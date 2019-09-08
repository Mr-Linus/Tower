from django.urls import path
from Task import views

app_name = 'Task'
urlpatterns = [
    path('', views.TaskView.as_view()),
    path('add', views.CreateTaskView.as_view()),
    path('detail/<str:namespace>/<str:name>', views.DetailTaskView.as_view()),
    path('delete/<str:namespace>/<str:name>', views.DeleteTaskView.as_view()),
    path('namespace/', views.NamespaceView.as_view()),
    path('namespace/delete/<str:name>/', views.DeleteNamespaceView.as_view()),
]
