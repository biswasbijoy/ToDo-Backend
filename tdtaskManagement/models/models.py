from django.db import models
from django.contrib.auth import get_user_model
from tdcore.models.models import BaseStampStampModel

User = get_user_model()

class Project(BaseStampStampModel) :
    name = models.CharField(max_length=512, unique=True)
    description = models.TextField(blank=True)
    project_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='project_project_manager')
    members = models.ManyToManyField(User, related_name='project_members')
    
    def __str__(self):
        return self.name
    
class Task(BaseStampStampModel) :
    TASK_STATUS_OPTION = (
        ("done", "Done"),
        ("active", "Active"),
        ("deleted", "Deleted"),
    )
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS_OPTION, default="active")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='task_project')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_created_by')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('name', 'project', 'created_by'), name='unique_name_project_created_by'),
        ]
        
        
    def __str__(self):
        return self.name