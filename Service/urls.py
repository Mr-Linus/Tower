from django.urls import path
from Service import views

app_name = 'Service'
urlpatterns = [
    path('', views.ServiceView.as_view()),
    path('delete/<str:name>/', views.DeleteServiceView.as_view()),
]
