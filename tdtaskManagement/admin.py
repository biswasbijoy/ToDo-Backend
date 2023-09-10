from django.contrib import admin
from tdtaskManagement.models.models import Project, Task

admin.site.register([Project, Task])
