from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/new/', views.book_create_update, name='book_create'),
    path('books/<int:pk>/edit/', views.book_create_update, name='book_update'),  # این URL برای ویرایش کتاب است
]
