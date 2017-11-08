from django.db import models


# Create your models here.
class Instructors(models.Model):
    name = models.CharField(verbose_name=u'Instructors Name', max_length=255, help_text='This is as name')
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    course = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
