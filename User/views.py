from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView
from django.contrib.auth.models import User
from .models import *
from .serialazers import *
from .utils import send_to_telegram
from rest_framework.permissions import IsAdminUser, AllowAny


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        send_to_telegram(contact)


class SubscribeAPIView(CreateAPIView):
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


class ProjectDetailAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





#ISADMIN
class ProjectCreateAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]

#ISADMIN
class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]



#ISADMIN
class ProjectDeleteAPIView(DestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAdminUser]


#ISADMIN
class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]






