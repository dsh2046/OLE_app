from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='City_name')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')
    desc = models.CharField(max_length=200, verbose_name='Description')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='Organization_name')
    desc = models.TextField(verbose_name='Description')
    tag = models.CharField(max_length=10, verbose_name='tag', default='famous')
    category = models.CharField(default='org', verbose_name='Org_category', max_length=20, choices=(('org','Organization'),('per','Personal'),('col', 'College')))
    click_num = models.IntegerField(default=0, verbose_name='Click_num')
    fav_nums = models.IntegerField(default=0, verbose_name='Favourite_Numbers')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='Logo', max_length=100)
    address = models.CharField(max_length=150, verbose_name='Address_name')
    city = models.ForeignKey(CityDict, verbose_name='City')
    students = models.IntegerField(default=0, verbose_name='Student_Numbers')
    course_nums = models.IntegerField(default=0, verbose_name='Course_Numbers')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'CourseOrg'
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        return self.teacher_set.all().count()

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='Organization')
    name = models.CharField(max_length=50, verbose_name='Teacher_name')
    work_years = models.IntegerField(default=0, verbose_name='Work_year')
    work_company = models.CharField(max_length=50, verbose_name='Work_company')
    work_position = models.CharField(max_length=50, verbose_name='Work_position')
    points = models.CharField(max_length=50, verbose_name='Points')
    click_num = models.IntegerField(default=0, verbose_name='Click_num')
    fav_nums = models.IntegerField(default=0, verbose_name='Favourite_Numbers')
    age = models.IntegerField(default=18, verbose_name='age')
    image = models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='Logo', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_course_nums(self):
        return self.course_set.all().count()
