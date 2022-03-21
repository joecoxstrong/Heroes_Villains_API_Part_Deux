from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('', views.super_types_list),

]
