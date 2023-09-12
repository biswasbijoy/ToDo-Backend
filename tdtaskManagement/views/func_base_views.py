import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from tdtaskManagement.models.models import Project
from tdtaskManagement.serializers.serializer import ProjectListSerializer
User = get_user_model()
logger = logging.getLogger(__name__)

@api_view(['GET'])
def project_list_api_view(request, *args, **kwargs) :
    try:
        project_queryset = Project.objects.all()
        serializer = ProjectListSerializer(project_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        logger.error(str(e), exc_info=True)
    return Response({"error": "INTERNAL SERVER ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def project_details_api_view(request, project_id, *args, **kwargs) :
    try:
        project_object = Project.objects.filter(pk=project_id).first()
        if not project_object:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        serializer = ProjectListSerializer(instance=project_object)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        logger.error(str(e), exc_info=True)
    return Response({"error": "INTERNAL SERVER ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)