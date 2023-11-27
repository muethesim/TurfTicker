from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('check-email', views.checkEmail),
    path('register', views.registerUser),
    path('login', views.loginUser),

    path('message', views.contact),
    
    path('check-slot', views.checkSlot),
    path('book-slot', views.bookSlot),
    path('cancel-slot', views.cancelSlot),
    path('edit-slot', views.editSlot),
    path('view-slot', views.viewSlot),

    path('chatbot', views.chatBot),
]