
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('msg/', views.front_end, name='msg')
]
