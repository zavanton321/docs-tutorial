from django.contrib import admin

from student.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)