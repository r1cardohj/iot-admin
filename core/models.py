from django.db import models

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


class Action(models.Model):
    """ iot model's action, eg. a light will
    have those action: `turn on` `turn off`,
    just like the ability of iot model
    """
    identifier = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=250)
    required = models.BooleanField()


class ActionData(models.Model):
    identifier = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=8, choices=DATA_TYPE)
    specs = models.JSONField()


class Event(models.Model):
    EVENT_TYPE = {
        "EVENT_TYPE_INFO": "INFO",
        "EVENT_TYPE_ALERT": "ALERT",
        "EVENT_TYPE_ERROR": "ERROR"
    }
    identifier = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40)


class EventData(models.Model):
    identifier = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    data_type = models.CharField(max_length=8, choices=DATA_TYPE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    specs = models.JSONField()


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
    version = models.CharField(max_length=10, defautl="0.0.1")

