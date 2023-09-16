import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from tdtaskManagement.models.models import Project
from tdtaskManagement.serializers.serializer import ProjectSerializer, ProjectCreateUpdateSerializer
User = get_user_model()
logger = logging.getLogger(__name__)

@api_view(['GET'])
def project_list_api_view(request, *args, **kwargs) :
    try:
        project_queryset = Project.objects.filter(status="active")
        serializer = ProjectSerializer(project_queryset, many=True)
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
        
        serializer = ProjectSerializer(instance=project_object)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        logger.error(str(e), exc_info=True)
    return Response({"error": "INTERNAL SERVER ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def project_create_api_view(request, *args, **kwargs) :
    try :
        data = request.data
        serializer = ProjectCreateUpdateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(str(e), exc_info=True)
    return Response({"error": "INTERNAL SERVER ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PATCH'])
def project_update_api_view(request, project_id, *args, **kwargs) :
    try :
        project_obj = Project.objects.filter(pk=project_id).first()
        
        if not project_obj:
            return Response([], status=status.HTTP_204_NO_CONTENT)
        
        serializer = ProjectCreateUpdateSerializer(instance=project_obj, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(str(e), exc_info=True)
    
    
    return Response({"error": "INTERNAL SERVER ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def project_delete_api_view(request, project_id, *args, **kwargs) :
    try :
        Project.objects.filter(id=project_id).update(status="deleted")
        return Response([], status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        logger.error(str(e), exc_info=True)
    return Response({"error": "INTERNAL SERVER ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)