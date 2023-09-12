from django.urls import path
from tdtaskManagement.views.views import HealthAPIView
from tdtaskManagement.views.func_base_views import project_list_api_view, project_details_api_view
urlpatterns = [
    path('ping/', HealthAPIView.as_view(), name='ping'),

]

func_base_urlpattern = [
    path('func_base_projet_list/', project_list_api_view, name='func_base_projet_list'),
    path('func_base_projet_details/<int:project_id>/', project_details_api_view, name='func_base_projet_details'),
]


urlpatterns += func_base_urlpattern