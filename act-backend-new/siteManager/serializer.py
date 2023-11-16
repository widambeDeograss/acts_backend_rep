from rest_framework import serializers
from .models import *


class EventGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'date',
            'time',
            'image',
            'created_at',
        ]
        depth = 2


class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'date',
            'time',
            'image',
        ]


class ApplicationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'document',
            'created_at'
        ]
        depth = 1


class ApplicationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'document',
        ]


class ContactGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'message',
            'name',
            'email',
            'created_at',
        ]
        depth = 1


class ContactPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'message',
            'name',
            'email',
            'created_at',
        ]

