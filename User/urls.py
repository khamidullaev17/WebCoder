from django.urls import path
from .views import *

urlpatterns = [
    path("contact/",ContactCreateAPIView.as_view()),
    path('subscribe/', SubscribeAPIView.as_view()),
    path("categories/", CategoryListAPIView.as_view()),
    path("projects/", ProjectListAPIView.as_view())
]



