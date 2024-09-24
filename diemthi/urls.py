# diemthi/urls.py

from django.urls import path
from .views import search_student

urlpatterns = [
    path('', search_student, name='search_student'),  # URL chính sẽ hiển thị trang tìm kiếm
]
