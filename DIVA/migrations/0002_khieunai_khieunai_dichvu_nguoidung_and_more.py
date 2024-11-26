# Generated by Django 5.1.3 on 2024-11-26 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DIVA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KhieuNai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=100)),
                ('sodienthoai', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('diachi', models.CharField(blank=True, max_length=200, null=True)),
                ('loai_khieu_nai', models.CharField(choices=[('DichVu', 'Dịch vụ'), ('LichHen', 'Lịch hẹn')], max_length=10)),
                ('ma_hoadon', models.CharField(blank=True, max_length=100, null=True)),
                ('ngay_su_dung', models.DateField()),
                ('tieude_khieu_nai', models.CharField(max_length=200)),
                ('mota_chitiet', models.TextField()),
                ('thoigian_xay_ra', models.DateTimeField()),
                ('nguoi_lien_quan', models.CharField(blank=True, max_length=100, null=True)),
                ('phuong_an_mong_muon', models.CharField(choices=[('HoanTien', 'Hoàn tiền'), ('SuaChua', 'Sửa chữa'), ('BoiThuong', 'Bồi thường'), ('GiaiThich', 'Giải thích rõ thêm')], max_length=20)),
                ('hoa_don_hoac_hop_dong', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('hinh_anh_video', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('cam_ket', models.BooleanField(default=False)),
            ],
            options={
                'permissions': [('can_view_khieu_nai', 'Can view khieu nại'), ('can_process_khieu_nai', 'Can process khieu nại'), ('can_edit_data_khieu_nai', 'Can edit du lieu don khieu nai'), ('can_create_khieu_nai', 'Can create don khieu nai')],
            },
        ),
        migrations.CreateModel(
            name='KhieuNai_DichVu',
            fields=[
                ('MaKN', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('noidung', models.TextField()),
                ('trangthaixuly', models.CharField(choices=[('Chua', 'Chưa xử lý'), ('Dang', 'Đang xử lý'), ('Da', 'Đã xử lý')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NguoiDung',
            fields=[
                ('MaUser', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=100)),
                ('VaiTro', models.CharField(choices=[('Nhân viên', 'Nhân viên'), ('Khách hàng', 'Khách hàng')], default='Khách hàng', max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='lichhen',
            options={'ordering': ['thoigiandangki']},
        ),
        migrations.CreateModel(
            name='LichHenDichVu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaDV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DIVA.dichvu')),
                ('MaLH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DIVA.lichhen')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('MaUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='DIVA.nguoidung')),
                ('hoten', models.CharField(max_length=50)),
                ('ngaysinh', models.DateField()),
                ('sodienthoai', models.IntegerField()),
                ('diachi', models.CharField(max_length=120)),
                ('is_Enable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='KhieuNaiLichHen',
            fields=[
                ('MaKN', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('NoiDung', models.TextField()),
                ('TrangThai', models.CharField(choices=[('Chưa xử lý', 'Chưa xử lý'), ('Đang xử lý', 'Đang xử lý'), ('Đã hoàn thành', 'Đã hoàn thành')], default='Chưa xử lý', max_length=20)),
                ('MaLH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DIVA.lichhen')),
                ('MaKH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='KH_KNLH', to='DIVA.nguoidung')),
                ('MaNV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NV_KNLH', to='DIVA.nguoidung')),
            ],
        ),
        migrations.CreateModel(
            name='DichVuDaDung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaDV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DIVA.dichvu')),
                ('MaKN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DIVA.khieunai_dichvu')),
                ('MaUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DIVA.nguoidung')),
            ],
        ),
        migrations.CreateModel(
            name='YeuCauTuVan',
            fields=[
                ('MaYCTV', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('TenKH', models.CharField(max_length=100)),
                ('SDT', models.CharField(max_length=10)),
                ('TrangThai', models.CharField(choices=[('Chưa xử lý', 'Chưa xử lý'), ('Đang xử lý', 'Đang xử lý'), ('Tư vấn lại', 'Tư vấn lại')], default='Chưa xử lý', max_length=20)),
                ('MaDV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DIVA.dichvu')),
                ('MaNV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NV_YCTV', to='DIVA.nguoidung')),
            ],
        ),
        migrations.CreateModel(
            name='YeuCau_DichVu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaDV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DIVA.dichvu')),
                ('MaYCTV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DIVA.yeucautuvan')),
            ],
        ),
    ]