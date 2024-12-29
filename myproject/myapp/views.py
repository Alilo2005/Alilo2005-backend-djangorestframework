from django.shortcuts import render
from rest_framework import generics
from .models import BOOK
from .serializers import BOOKSerializer
# Create your views here.
class BOOKListCreateView(generics.ListCreateAPIView):
    queryset = BOOK.objects.all()
    serializer_class = BOOKSerializer

class BOOKListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BOOK.objects.all()
    serializer_class = BOOKSerializer