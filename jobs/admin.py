from django.contrib import admin
from .models import *
# Register your models here.


# Job.objects.all().delete()
# Projects.objects.all().delete()
# Education.objects.all().delete()
# Skills.objects.all().delete()
# Accomplishments.objects.all().delete()

admin.site.register(Job)
admin.site.register(Projects)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Accomplishments)