from django.urls import path
from Image import views

app_name = 'Image'
urlpatterns = [
    path('nodes/list', views.NodeListView.as_view()),
]
