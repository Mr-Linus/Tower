from django.urls import path
from Task import views

app_name = 'Task'
urlpatterns = [
    path('namespace/', views.NamespaceView.as_view()),
    path('namespace/delete/<str:name>/', views.DeleteNamespaceView.as_view()),
]
