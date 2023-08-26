from rest_framework import viewsets

from person.serializers import PersonSerializer
from person.models import Person


class PersonView(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
