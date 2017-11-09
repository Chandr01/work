from django.db import models
from django.conf import settings


# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Instructors(models.Model):
    name = models.CharField(verbose_name=u'Instructors Name', max_length=255, help_text='This is as name')
    surname = models.CharField(verbose_name=u'Second name', max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    course = models.ManyToManyField(Course, null=True)
    slug = models.SlugField(default='False')
    is_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f', 'Female')), default='m')
    position = models.ForeignKey(Position, null=True)
    # position = models.CharField(choices=(('i', 'Instructor'), ('a', 'Assistent')), max_length=1)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True)

    def __str__(self):
        return self.name
