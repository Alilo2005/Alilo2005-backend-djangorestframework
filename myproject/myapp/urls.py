from django.urls import path
from .views import BOOKListCreateView, BOOKListRetrieveUpdateDestroyView

urlpatterns = [
    path('books/', BOOKListCreateView.as_view(), name='book-list-create'),  # List and create books
    path('books/<int:pk>/', BOOKListRetrieveUpdateDestroyView.as_view(), name='book-detail'),  # Retrieve, update, delete book
]
