from rest_framework import generics
from .serializer import ContactSerializer, ContactInfoSerializer
from .models import Contact, ContactInfo


# Create your views here.


class ContactInfoView(generics.ListAPIView):
    queryset = ContactInfo.objects.all().order_by('-id')[:1]
    serializer_class = ContactInfoSerializer


class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
