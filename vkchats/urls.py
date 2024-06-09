from django.urls import path
from .views import home_view,vkchats_view,chat_view

urlpatterns = [
    path('', home_view, name='home-page'),
    path('vkchats/',vkchats_view,name='vkchats-page'),
    path('vkchats/<int:page_number>/', vkchats_view, name='vkchats-page-num'),
    path('chat/<slug:slug>',chat_view,name='chat-page'),
]
