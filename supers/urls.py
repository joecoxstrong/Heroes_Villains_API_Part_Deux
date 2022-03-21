from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.super_list),
    # path('<int:pk>/', view.super_types_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)