from django.urls import re_path
from _crud import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^funcionario$',views.funcionario_Api),
    re_path(r'^funcionario/([0-9]+)$',views.funcionario_Api),

    re_path(r'^funcionario/savefile',views.SaveFile),
    
    re_path(r'^atividade$',views.atividade_Api),
    re_path(r'^atividade$/([0-9]+)$',views.atividade_Api)
    
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)