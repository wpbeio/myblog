# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser


# 用来修改admin中显示的app名称,因为admin app 名称是用 str.title()显示的,所以修改str类的title方法就可以实现.
# class string_with_title(str):
#     def __new__(cls, value, title):
#         instance = str.__new__(cls, value)
#         instance._title = title
#         return instance

#     def title(self):
#         return self._title

#     __copy__ = lambda self: self
#     __deepcopy__ = lambda self, memodict: self


# Create your models here.
class BeioUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None):
        """
        保存用户，测试是否是邮箱
        """
        if not email:
            raise ValueError('必须使用正确的邮箱')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class BeioUser(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    email = models.EmailField(
        verbose_name='邮箱地址',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    createdate = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    img = models.CharField(max_length=200, default='/static/images/tx/default.jpg',
                           verbose_name=u'头像地址')
    intro = models.CharField(max_length=200, blank=True, null=True,
                             verbose_name=u'简介')
    USERNAME_FIELD='username'
    # REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    # class Meta(User.Meta):
    #     # auto_created = True
    #     verbose_name_plural = verbose_name = u"注册用户"
    #     # db_table='auth_user'
    #     # app_label = string_with_title('beio_auth', u"用户管理")
