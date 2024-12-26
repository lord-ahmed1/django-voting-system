from django.urls import path
from . import views
urlpatterns=[path("validate cpf/",views.checkCPF,name="check cpf")]
