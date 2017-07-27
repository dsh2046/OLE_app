from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course


class UserAsk(models.Model):
    name = models.CharField(max_length=50, verbose_name='User_name')
    mobile = models.CharField(max_length=10, verbose_name='Mobile')
    course_name = models.CharField(max_length=50, verbose_name='Course_name')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'UserAsk'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='User')
    course = models.ForeignKey(Course, verbose_name='Course')
    comments = models.CharField(max_length=200, verbose_name='Comments')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='User')
    fav_id = models.IntegerField(default=0, verbose_name='Fav_id')
    fav_type = models.IntegerField(choices=((1, 'Course'),(2, 'Organization'),(3, 'Teacher')), default=1, verbose_name='Fav_type')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'UserFavorite'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name='UserMessage_id')
    message = models.CharField(max_length=500, verbose_name='Message')
    has_read = models.BooleanField(default=False, verbose_name='Has_read')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'UserMessage'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='User')
    course = models.ForeignKey(Course, verbose_name='Course')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'UserCourse'
        verbose_name_plural = verbose_name


