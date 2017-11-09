from django.contrib import admin
from instructors.models import Instructors, Position, Course

# Register your models here.
admin.site.register(Instructors)
admin.site.register(Position)
admin.site.register(Course)