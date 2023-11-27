from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login-page'),

    path('order-page', views.orderPage, name='order-page'),
    path('user-page', views.userPage, name='user-page'),
    path('statistic-page', views.statisticPage, name='statistic-page'),
    path('profile-page', views.profilePage, name='profile-page'),
    path('inbox-page', views.inboxPage, name='inbox-page'),
    path('slot-page', views.slotPage, name='slot-page'),
]