from django.db import models

class Student(models.Model):
    sbd = models.CharField(max_length=10, unique=True)  # Số báo danh
    toan = models.FloatField(null=True)        # Điểm Toán
    ngu_van = models.FloatField(null=True)     # Điểm Ngữ Văn
    ngoai_ngu = models.FloatField(null=True)   # Điểm Ngoại Ngữ
    vat_li = models.FloatField(null=True)      # Điểm Vật Lý
    hoa_hoc = models.FloatField(null=True)     # Điểm Hóa Học
    sinh_hoc = models.FloatField(null=True)    # Điểm Sinh Học
    lich_su = models.FloatField(null=True)      # Điểm Lịch Sử
    dia_li = models.FloatField(null=True)       # Điểm Địa Lý
    gdcd = models.FloatField(null=True)         # Điểm Giáo Dục Công Dân
    ma_ngoai_ngu = models.CharField(max_length=10, null=True)  # Mã Ngoại Ngữ
