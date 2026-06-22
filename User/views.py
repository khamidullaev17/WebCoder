from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Contact, Subscriber, Category, Project
from .serialazers import ContactSerializer, SubscriberSerializer, CategorySerializer, ProjectSerializer
from .utils import send_to_telegram



class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        send_to_telegram(contact)



class SubscribeAPIView(generics.CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer



class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProjectListAPIView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(category__name__iexact=category)
        return queryset




