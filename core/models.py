from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DATA_TYPE = {
    'INT': 'int',
    'REAL': 'float',
    'TEXT': 'str',
    'DATE': 'date',
    'ENUM': 'enum',
    'BOOL': 'bool',
    'ARRAY': 'list',
    'OBJECT': 'dict'
}

class Property(models.Model):
    """ property is a kv data about iotModel
    """
    identifier = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40)
    data_type = models.CharField(max_length=8,
                                 choices=DATA_TYPE,
                                 default=DATA_TYPE['TEXT'])
    required = models.BooleanField()
    specs = models.JSONField()
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}(self.identifier)"


class Action(models.Model):
    """ iot model's action, eg. a light will
    have those action: `turn on` `turn off`,
    just like the ability of iot model
    """
    identifier = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=250)
    required = models.BooleanField()
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}(self.identifier)"


class ActionData(models.Model):
    identifier = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=8, choices=DATA_TYPE)
    specs = models.JSONField()
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}(self.identifier)"


class Event(models.Model):
    EVENT_TYPE = {
        "EVENT_TYPE_INFO": "INFO",
        "EVENT_TYPE_ALERT": "ALERT",
        "EVENT_TYPE_ERROR": "ERROR"
    }
    identifier = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}(self.identifier)"


class EventData(models.Model):
    identifier = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    data_type = models.CharField(max_length=8, choices=DATA_TYPE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    specs = models.JSONField()
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}(self.identifier)"

class Schema(models.Model):
    """ a basic device class in iot platform,
    it describes what an model/device can do 
    and what it has.
    """
    identifier = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40)
    properties = models.ManyToManyField(Property)
    events = models.ManyToManyField(Event)
    actions = models.ManyToManyField(Action)
    version = models.CharField(max_length=10,default="0.0.1")
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}(self.identifier)"


class Product(models.Model):
    PRODUCT_TYPE = {
        "GATEWAY_DEVICE": "gateway",
        "GATEWAY_SUB_DEVICE": "sub",
        "DIRECT_DEVICE": "direct"
    }

    identifier = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=18, choices=PRODUCT_TYPE)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}(self.identifier)"


class Device(models.Model):
    identifier = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # parent always gateway device
    parent_device = models.ForeignKey('self',
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      blank=True,
                                      related_name='children')

    ip_addr = models.CharField(max_length=36, blank=True, null=True)
    online = models.BooleanField(default=False)
    port = models.CharField(max_length=5, blank=True, null=True)
    location = models.JSONField()
    description = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}(self.identifier)"


class DeviceShadow(models.Model):
    """ a shadow about device, show some
    real time information about device
    """
    LOCK = {
        'LOCKED': 'locked',
        'UNLOCK': 'unlock'
    }
    device = models.OneToOneField(Device,
                                  on_delete=models.CASCADE,
                                  related_name='shadow')
    state = models.JSONField()
    desired_state = models.JSONField()
    reported_state = models.JSONField()

    version = models.IntegerField(default=0)
    last_updated_dt = models.DateTimeField(auto_now=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    online = models.BooleanField(default=False)
    last_connected_at = models.DateTimeField()
    lock_status = models.CharField(max_length=6, choices=LOCK)
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Topic(models.Model):
    """ the key of Pub/Sub model
    """
    identifier = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    product_pattern = models.CharField(max_length=100)
    device_pattern = models.CharField(max_length=100)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}(self.identifier)"
