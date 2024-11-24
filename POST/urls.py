from django.urls import path
from . import views

app_name = 'POST'

urlpatterns = [
    path('<str:slug>', views.post, name="PAGE")
]
