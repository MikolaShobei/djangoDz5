from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from user_profile.serializers import UserProfileSerializer, ProfileCreateSerializer

UserModel = get_user_model()


class CustomSerializer(ModelSerializer):
    profile = UserProfileSerializer(read_only=True, required=False)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'created', 'updated', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user


class UserSerializerForStaff(ModelSerializer):
    profile = UserProfileSerializer(read_only=True, required=False)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'is_active', 'is_staff', 'created', 'updated', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user


class UpdateByUserSerializer(ModelSerializer):
    profile = ProfileCreateSerializer()

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'profile']

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile')
        instance.profile.name = profile.get('name', instance.profile.name)
        instance.profile.surname = profile.get('surname', instance.profile.surname)
        instance.profile.age = profile.get('age', instance.profile.age)
        instance.save()

        return super().update(instance, validated_data)


class UpdateByStaffSerializer(ModelSerializer):
    #  Більшу кількість серіалайзерів я створив для того щоб щоб лише
    #  адмін міг зробити юзера адміном, а не сам юзер коли захоче

    profile = ProfileCreateSerializer()

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'is_staff', 'is_active', 'profile']

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile')
        instance.profile.name = profile.get('name', instance.profile.name)
        instance.profile.surname = profile.get('surname', instance.profile.surname)
        instance.profile.age = profile.get('age', instance.profile.age)
        instance.save()

        return super().update(instance, validated_data)
