from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('showmemes',views.showmemes,name='showmemes'),
    path('memepage',views.memepage,name='memepage')
]