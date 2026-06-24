from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *



urlpatterns = [
    # contact
    path("contact/", ContactCreateAPIView.as_view()), #POST
    # email
    path("subscribe/", SubscribeAPIView.as_view()), #POST
    # Auth
    path("register/", RegisterAPIView.as_view()), #POST
    path("login/", TokenObtainPairView.as_view()), #POST
    path("token/refresh/", TokenRefreshView.as_view()), #POST
    #LOOK
    path("categories/", CategoryListAPIView.as_view()), #GET
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view()),
    path("projects/", ProjectListAPIView.as_view()), #GET
    path("projects/<int:pk>/", ProjectDetailAPIView.as_view()),
    #CREATE
    path("projects/create/", ProjectCreateAPIView.as_view()), #POST
    path("categories/create/",CategoryCreateAPIView.as_view()), #POST
    #DELETE
    path("projects/<int:pk>/delete/", ProjectDeleteAPIView.as_view()), #DELETE
    path("categories/<int:pk>/delete/",CategoryDeleteAPIView.as_view()) #DELETE
]



