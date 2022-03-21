from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.super_types_list),
    path('<int:pk>/', views.super_types_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)