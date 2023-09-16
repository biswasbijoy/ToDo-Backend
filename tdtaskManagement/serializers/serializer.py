from rest_framework.serializers import ModelSerializer
from tdtaskManagement.models.models import Project
from tdauth.serializers.serializers import UserUserNameEmailSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ProjectSerializer(ModelSerializer) :
    members = UserUserNameEmailSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = "__all__"
        
class ProjectCreateUpdateSerializer(ModelSerializer) :
    class Meta:
        model = Project
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["project_manager"] = {
            "id": instance.project_manager.id,
            "username": instance.project_manager.username,
            "email": instance.project_manager.email,
        }
    
        members_qs = User.objects.filter(project_members__id=instance.id)
        member_response = UserUserNameEmailSerializer(instance=members_qs, many=True)
        response["members"] = member_response.data
        return response
