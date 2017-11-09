from django.contrib import admin
from instructors.models import Instructors, Position, Course
from django.db import models
from django.forms import widgets


# Register your models here.
class InstructorInline(admin.StackedInline):
    model = Instructors
    fields = ['name']


class PositionAdmin(admin.ModelAdmin):
    inlines = [InstructorInline]


class InstructorsAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", 'is_active', 'position']
    list_display_links = ["name", "surname"]
    list_filter = ['is_active', 'position']
    search_fields = ["name", "surname"]
    list_editable = ['is_active']
    # fields = [ "name", "surname", "email", 'date_of_birth', 'is_active', 'position']
    # exclude = ['date_of_birth']
    # readonly_fields = ['is_active']
    raw_id_fields = ['position']
    save_as = True
    save_on_top = True
    fieldsets = [
        ('Main inform', {'fields': ["name", "surname"]}),
        ('Other information', {'fields': ["email", 'date_of_birth', 'is_active', 'position'],
                               'classes': ['collapse']}),
    ]

    formfield_overrides = {
        models.DateField: {'widget': widgets.TextInput}
    }


admin.site.register(Instructors, InstructorsAdmin)
# admin.site.register(Instructors)
admin.site.register(Position, PositionAdmin)
admin.site.register(Course)
