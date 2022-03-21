from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.super_list),
    path('<int:pk>/', views.super_detail),
    path('supers?type=<type>/',views.super_list)
]

urlpatterns = format_suffix_patterns(urlpatterns)