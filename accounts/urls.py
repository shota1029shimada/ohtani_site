from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from . import views
#from .views import SignupView

app_name='accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # ユーザー登録
   # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # ログイン
     #path('signup/',SignupView.as_view(), name='signup'),

]