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


class StaffPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = [
            'full_name',
            'titles',
            'image',
            'education',
        ]


class StaffGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
        depth = 2


class CoursePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'category',
            'course',
        ]


class CourseGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        depth = 2


class AdministrationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administration
        fields = [
            'admin_title',
            'staff_name',
            'staff_titles',
            'image',
        ]


class AdministrationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administration
        fields = "__all__"
        depth = 2


class MastersCostTablePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MastersCostTable
        fields = [
            'description',
            'units',
            'price_per_unit',
            'total_price',
            'type',
        ]


class MastersCostTableGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MastersCostTable
        fields = "__all__"
        depth = 2


class PhdCostTablePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhdCostTable
        fields = [
            'course',
            'description',
            'amount',
        ]


class PhdCostTableGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhdCostTable
        fields = "__all__"
        depth = 2


class ImportantInformationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantInformation
        fields = [
            'mission',
            'vision',
            'message_from_president',
            'historical_background',
        ]


class ImportantInformationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantInformation
        fields = "__all__"
        depth = 1


class GalleryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = [
            'type',
            'title',
            'file',
        ]


class GalleryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"
        depth = 1
