from django.urls import path
from tdtaskManagement.views.views import HealthAPIView
urlpatterns = [
    path('ping/', HealthAPIView.as_view(), name='ping'),

]