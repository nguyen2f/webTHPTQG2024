import os
import django
import mysql.connector
from diemthi.models import Student  # Đảm bảo 'diemthi' là tên ứng dụng chính xác

# Thiết lập môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')  # Thay 'mywebsite' bằng tên dự án của bạn
django.setup()

def import_students():
    # Kết nối đến cơ sở dữ liệu MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',           # Tên người dùng MySQL
        password='admin',      # Mật khẩu của người dùng MySQL
        database='thptqg2024'  # Tên cơ sở dữ liệu của bạn
    )

    cursor = conn.cursor()

    # Truy vấn để lấy dữ liệu từ bảng MySQL
    cursor.execute("SELECT sbd, toan, ngu_van, ngoai_ngu, vat_li, hoa_hoc, sinh_hoc, lich_su, dia_li, gdcd, ma_ngoai_ngu FROM your_table_name")  # Thay 'your_table_name' bằng tên bảng của bạn

    for row in cursor.fetchall():
        # Tạo một đối tượng Student cho mỗi hàng dữ liệu
        student = Student(
            sbd=row[0],
            toan=row[1],
            ngu_van=row[2],
            ngoai_ngu=row[3],
            vat_li=row[4],
            hoa_hoc=row[5],
            sinh_hoc=row[6],
            lich_su=row[7],
            dia_li=row[8],
            gdcd=row[9],
            ma_ngoai_ngu=row[10],
        )
        student.save()  # Lưu đối tượng vào cơ sở dữ liệu Django

    # Đóng kết nối
    cursor.close()
    conn.close()

if __name__ == "__main__":
    import_students()
