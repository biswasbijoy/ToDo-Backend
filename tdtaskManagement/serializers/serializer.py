from rest_framework.serializers import ModelSerializer
from tdtaskManagement.models.models import Project
from tdauth.serializers.serializers import UserUserNameEmailSerializer

class ProjectListSerializer(ModelSerializer) :
    members = UserUserNameEmailSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = "__all__"

