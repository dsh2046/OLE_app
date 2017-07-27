from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from organization.models import CourseOrg, Teacher


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name='course_org', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, verbose_name='teacher', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='coursename')
    desc = models.CharField(max_length=300, verbose_name='description')
    detail = models.TextField(verbose_name='Detail')
    is_banner = models.BooleanField(default=False, verbose_name='is_banner')
    degree = models.CharField(max_length=10, choices=(('Easy', 'Easy'),('Medium', 'Medium'),('Hard', 'Hard')))
    learn_time = models.IntegerField(default=0, verbose_name='Learn_time(Minutes)')
    students = models.IntegerField(default=0, verbose_name='Amounts of students')
    fav_nums = models.IntegerField(default=0, verbose_name='Favourite_Numbers')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='Title_Images', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='Click_Nums')
    category = models.CharField(default='Backend_develop', max_length=20, verbose_name='category')
    tag = models.CharField(default='', verbose_name='course_tag', max_length=10)
    need_know = models.CharField(max_length=300, verbose_name='need_know', default='')
    teacher_tell = models.CharField(max_length=300, verbose_name='teacher_tell', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = verbose_name

    def get_chapter_amount(self):
        return self.lesson_set.all().count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='Course')
    name = models.CharField(max_length=100, verbose_name='Chapter_name')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_video(self):
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='Chapter')
    name = models.CharField(max_length=100, verbose_name='Video_name')
    url = models.CharField(max_length=200, verbose_name='Video_url', default='')
    learn_time = models.IntegerField(default=0, verbose_name='Learn_time(Minutes)')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='Course')
    name = models.CharField(max_length=100, verbose_name='Course_name')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='Download_file', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Add_time')

    class Meta:
        verbose_name = 'Resource'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

