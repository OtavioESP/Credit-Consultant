from rest_framework import serializers

from person.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'full_name',
            'email',
            'adress',
            'cpf',
            'rg'
        ]
