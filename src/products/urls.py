from django.urls import path
from .views import say_hello,Time
urlpatterns = [
    path('say-hi/<str:name>', say_hello),
    path('time', Time),
]
