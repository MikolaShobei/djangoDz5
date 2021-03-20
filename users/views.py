from sqlite3 import IntegrityError

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, get_object_or_404, UpdateAPIView, RetrieveAPIView, \
    DestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user_profile.serializers import UserProfileSerializer
from users.serializers import CustomSerializer, UserSerializerForStaff, UpdateByStaffSerializer, UpdateByUserSerializer

UserModel = get_user_model()


class CreateUserView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CustomSerializer
    permission_classes = [AllowAny]


class ListUsersView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CustomSerializer
    permission_classes = [IsAuthenticated]


class AddProfileView(CreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        print(self.request.user.id)
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)


class FullOwnInfoView(RetrieveAPIView):
    serializer_class = CustomSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        print(self.request.user)
        return self.request.user


class MakeStaffView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializerForStaff(instance, {'is_staff': True, 'is_active': True}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class DeleteUserView(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CustomSerializer
    permission_classes = [IsAdminUser]


class UpdateUserByUserView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateByUserSerializer

    def get_object(self):
        return self.request.user


class UpdateByStaffView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UpdateByStaffSerializer
