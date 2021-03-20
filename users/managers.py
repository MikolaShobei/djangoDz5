from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_kwargs):
        if not email:
            raise ValueError('email must have set username')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **extra_kwargs):
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_active', True)

        if extra_kwargs.get('is_active') is not True:
            raise ValueError('User must have is_active=rue')
        if extra_kwargs.get('is_superuser') is not True:
            raise ValueError('User must have is_superuser=rue')
        return self.create_user(**extra_kwargs)
