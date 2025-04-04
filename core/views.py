from core.models import Property
from core.models import Action
from core.models import Event
from core.models import Schema
from core.models import ActionData
from core.models import EventData
from core.serializers import PropertySerializer
from core.serializers import ActionSerializer
from core.serializers import EventSerializer
from core.serializers import SchemaSerializer
from core.serializers import ActionDataSerializer
from core.serializers import EventDataSerializer
from rest_framework import viewsets

# Create your views here.
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('-created_dt')
    serializer_class = PropertySerializer


class ActionDataViewSet(viewsets.ModelViewSet):
    queryset = ActionData.objects.all().order_by('-created_dt')
    serializer_class = ActionDataSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all().order_by('-created_dt')
    serializer_class = ActionSerializer


class EventDataViewSet(viewsets.ModelViewSet):
    queryset = EventData.objects.all().order_by('-created_dt')
    serializer_class = EventDataSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-created_dt')
    serializer_class = EventSerializer


class SchemaViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all().order_by('-created_dt')
    serializer_class = SchemaSerializer