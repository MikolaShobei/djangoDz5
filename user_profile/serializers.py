from rest_framework.serializers import ModelSerializer

from user_profile.models import ProfileModel


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'avatar')


class ProfileCreateSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age')
