import os
import django

# Cấu hình biến môi trường
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')
django.setup()

import mysql.connector
from diemthi.models import Student
def convert_to_float(value):
    """Chuyển đổi giá trị thành float hoặc trả về None nếu là chuỗi rỗng."""
    try:
        return float(value) if value else None
    except ValueError:
        return None
# Kết nối đến MySQL
cnx = mysql.connector.connect(
    user='root',
    password='admin',
    host='localhost',
    database='thptqg2024'
)

cursor = cnx.cursor()

# Lấy dữ liệu từ MySQL
query = "SELECT sbd, toan, ngu_van, ngoai_ngu, vat_li, hoa_hoc, sinh_hoc, lich_su, dia_li, gdcd, ma_ngoai_ngu FROM diem_thi_thpt_2024"
cursor.execute(query)

for (sbd, toan, ngu_van, ngoai_ngu, vat_li, hoa_hoc, sinh_hoc, lich_su, dia_li, gdcd, ma_ngoai_ngu) in cursor:
    student = Student(
        sbd=sbd,
        toan=convert_to_float(toan),
        ngu_van=convert_to_float(ngu_van),
        ngoai_ngu=convert_to_float(ngoai_ngu),
        vat_li=convert_to_float(vat_li),
        hoa_hoc=convert_to_float(hoa_hoc),
        sinh_hoc=convert_to_float(sinh_hoc),
        lich_su=convert_to_float(lich_su),
        dia_li=convert_to_float(dia_li),
        gdcd=convert_to_float(gdcd),
        ma_ngoai_ngu=ma_ngoai_ngu if ma_ngoai_ngu else None
    )
    student.save()

# Đóng kết nối
cursor.close()
cnx.close()