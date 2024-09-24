# diemthi/views.py

from django.shortcuts import render, get_object_or_404
from .models import Student

def search_student(request):
    student = None  # Khởi tạo biến student là None
    if request.method == 'GET':
        sbd = request.GET.get('sbd', None)
        if sbd:
            student = get_object_or_404(Student, sbd=sbd)  # Tìm kiếm thí sinh theo SBD
    return render(request, 'diemthi/search.html', {'student': student})
