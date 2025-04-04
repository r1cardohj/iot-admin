from core.models import Schema
from core.models import Action
from core.models import ActionData
from core.models import Event
from core.models import EventData
from core.models import Property
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class ActionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionData
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'


class EventDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventData
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class SchemaSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(read_only=True, many=True)
    events = EventSerializer(read_only=True, many=True)
    actions = ActionSerializer(read_only=True, many=True)
    class Meta:
        model = Schema
        fields = '__all__'
