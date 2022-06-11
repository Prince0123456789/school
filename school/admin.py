from django.contrib import admin

from school.models import notice, principal, student, teacher

# Register your models here.
admin.site.register(principal)
admin.site.register(teacher)
admin.site.register(student)
admin.site.register(notice)