# diemthi/views.py

from django.shortcuts import render, get_object_or_404
from .models import Student

'''def search_student(request):
    student = None  # Khởi tạo biến student là None
    if request.method == 'GET':
        sbd = request.GET.get('sbd', None)
        if sbd:
            student = get_object_or_404(Student, sbd=sbd)  # Tìm kiếm thí sinh theo SBD
    return render(request, 'diemthi/search.html', {'student': student})
'''

def search_student(request):
    sbd = request.GET.get('sbd')  # Get the SBD from the form submission
    try:
        # Try to find the student in the database
        student = Student.objects.get(sbd=sbd)
        return render(request, 'diemthi/search.html', {'student': student})
    except Student.DoesNotExist:
        # If the student does not exist, return the same page with an error message
        return render(request, 'diemthi/search.html', {'error_message': "Số báo danh không hợp lệ. Vui lòng nhập lại!"})
