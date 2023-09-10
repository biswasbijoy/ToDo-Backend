from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HealthAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try :
            response = {
                "message" : "Server is up and running",
                "version" : "v1.0.0"
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)