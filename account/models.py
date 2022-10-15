from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, name, username, email, password=None):
        if not name:
            raise ValueError('이름을 입력해야 합니다.')
        if not username:
            raise ValueError('닉네임을 입력해야 합니다.')
        if not email:
            raise ValueError('이메일을 입력해야 합니다.')
        user = self.model(
            name=name,
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, name, username, email, password=None):
        user = self.create_user(
            name=name,
            username=username,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        # user.is_staff = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=20, null=False, blank=False)
    username = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.username
