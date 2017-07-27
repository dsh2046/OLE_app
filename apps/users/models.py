from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='Nickname', default='')
    birthday = models.DateTimeField(verbose_name='Birthday', null=True)
    gender = models.CharField(max_length=20, choices=(('male', 'Male'),('female', 'Female')), default='female')
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = 'UserInfo'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

    # Get unread news' number
    def unread_nums(self):
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='VerifyCode')
    email = models.EmailField(max_length=50, verbose_name='Email')
    send_type = models.CharField(choices=(('register','Register'),('forget','Forget'),('update','Update')), max_length=20)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'EmailVerify'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='Banner_Pic', max_length=100)
    url = models.URLField(max_length=200, verbose_name='VisitAddress')
    index = models.IntegerField(default=100, verbose_name='Index')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_Time')

    class Meta:
        verbose_name = 'Banner_Pic'
        verbose_name_plural = verbose_name