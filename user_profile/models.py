from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# Create your models here.
def to_upload(instance, filename):
    return f'{instance.user.email}/avatars/{filename}'


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=to_upload)
