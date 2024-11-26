from django import forms
from .models import LichHen
from .models import KhieuNai
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DangKyForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LichHenForm(forms.ModelForm):
    class Meta:
        model = LichHen
        fields = ['MaKH', 'MaNV', 'MaDV', 'thoigiandangki']
        widgets = {
            'thoigiandangki': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'MaKH': 'Khách hàng',
            'MaNV': 'Nhân viên phụ trách',
            'MaDV': 'Dịch vụ',
            'thoigiandangki': 'Ngày đăng ký',
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.MaKH = self.request.user  # Gán MaKH là người dùng hiện tại
            instance.save()
        return instance

class CapNhatLichHenForm(forms.ModelForm):
    class Meta:
        model = LichHen
        fields = ['TrangThai']
        labels = {
            'TrangThai': 'Trạng thái',
        }

class KhieuNaiForm(forms.Form):
    # Thông tin khách hàng
    ten = forms.CharField(max_length=100, label='Họ và tên', required=True, widget=forms.TextInput(attrs={'placeholder': 'Nhập họ và tên'}))
    sodienthoai = forms.CharField(max_length=15, label='Số điện thoại liên lạc', required=True, widget=forms.TextInput(attrs={'placeholder': 'Nhập số điện thoại'}))
    email = forms.EmailField(max_length=100, label='Email', required=False, widget=forms.EmailInput(attrs={'placeholder': 'Nhập email'}))
    diachi = forms.CharField(max_length=200, label='Địa chỉ', required=False, widget=forms.TextInput(attrs={'placeholder': 'Nhập địa chỉ'}))

    # Thông tin dịch vụ/sản phẩm khiếu nại
    loai_khieu_nai = forms.ChoiceField(
        choices=[('DichVu', 'Dịch vụ'), ('LichHen', 'Lịch hẹn')],
        label='Loại dịch vụ/sản phẩm khiếu nại',
        required=True,
        widget=forms.Select()
    )
    ma_hoadon = forms.CharField(max_length=100, label='Mã hóa đơn/số hợp đồng (nếu có)', required=False)
    ngay_su_dung = forms.DateField(label='Ngày sử dụng dịch vụ/sản phẩm', required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    # Nội dung khiếu nại
    tieude_khieu_nai = forms.CharField(max_length=200, label='Tiêu đề khiếu nại', required=True, widget=forms.TextInput(attrs={'placeholder': 'Ví dụ: Dịch vụ giao hàng chậm'}))
    mota_chitiet = forms.CharField(label='Mô tả chi tiết', required=True, widget=forms.Textarea(attrs={'placeholder': 'Mô tả chi tiết vấn đề gặp phải', 'rows': 4}))
    thoigian_xay_ra = forms.DateTimeField(label='Thời gian xảy ra sự việc', required=True, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    nguoi_lien_quan = forms.CharField(max_length=100, label='Người liên quan (nếu có)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Nhập tên hoặc chức vụ'}))

    # Yêu cầu giải quyết
    phuong_an_mong_muon = forms.ChoiceField(
        choices=[('HoanTien', 'Hoàn tiền'), ('SuaChua', 'Sửa chữa'), ('BoiThuong', 'Bồi thường'), ('GiaiThich', 'Giải thích rõ thêm')],
        label='Phương án mong muốn',
        required=True,
        widget=forms.Select()
    )

    # Tài liệu đính kèm
    hoa_don_hoac_hop_dong = forms.FileField(
        label='Tải lên hóa đơn hoặc hợp đồng',
        required=False,
        widget=forms.ClearableFileInput(attrs={'accept': '.pdf,.jpeg,.png,.jpg'})
    )
    hinh_anh_video = forms.FileField(
        label='Tải lên hình ảnh/video chứng minh',
        required=False,
        widget=forms.ClearableFileInput(attrs={'accept': '.jpg,.jpeg,.png,.mp4,.mov,.avi', 'max_size': '10485760'})
    )

    # Cam kết và xác nhận
    cam_ket = forms.BooleanField(
        label='Tôi cam kết rằng các thông tin trên là chính xác và chịu trách nhiệm nếu có sai sót.',
        required=True
    )

    # Nút gửi khiếu nại
    submit_button = forms.CharField(widget=forms.HiddenInput(), initial='Gửi khiếu nại')

    class Meta:
        fields = [
            'ten', 'sodienthoai', 'email', 'diachi',
            'loai_khieu_nai', 'ma_hoadon', 'ngay_su_dung',
            'tieude_khieu_nai', 'mota_chitiet', 'thoigian_xay_ra',
            'nguoi_lien_quan', 'phuong_an_mong_muon',
            'hoa_don_hoac_hop_dong', 'hinh_anh_video', 'cam_ket'
        ]
