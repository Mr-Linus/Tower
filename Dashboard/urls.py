from django.urls import path
from Dashboard import views

app_name = 'Dashboard'
urlpatterns = [
    path('', views.DashboardIndexView.as_view()),
]
