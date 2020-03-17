from django.contrib.auth.models import User
from rest_framework import serializers
from backend.models import Lover, City, Gender, Photo


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = 'id', 'name'


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = 'id', 'code', 'label'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username', 'email'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = 'file_path'


class LoverSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    gender = GenderSerializer()
    target_gender = GenderSerializer()
    user = UserSerializer()
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Lover
        fields = 'name', 'description', 'birthdate', 'gender', 'city', 'target_gender', 'age_min', 'age_max', 'photos'