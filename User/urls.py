from django.urls import path
from User import views

app_name = 'User'
urlpatterns = [
    path('login/', views.UserLoginView.as_view()),
    path('logout/', views.UserLogoutView.as_view()),
    path('sign-up/', views.add_user_view),
    path('', views.UserLoginView.as_view())
]
