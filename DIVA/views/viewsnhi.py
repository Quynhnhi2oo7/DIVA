from django.shortcuts import render, redirect
from ..forms import DangKyForm
from ..forms import KhieuNaiForm
# Create your views here.


def dang_ky(request):
    if request.method == 'POST':
        form = DangKyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dang-nhap')  # Chuyển hướng sau khi đăng ký thành công
    else:
        form = DangKyForm()
    return render(request, 'auth/dang_ky.html', {'form': form})



def khieu_nai(request):
    if request.method == 'POST':
        form = KhieuNaiForm(request.POST, request.FILES)
        if form.is_valid():
            # Lưu khiếu nại vào cơ sở dữ liệu (nếu cần)
            form.save()
            return render(request, '')  # Redirect đến trang thành công
    else:
        form = KhieuNaiForm()

    return render(request, 'khieu_nai/khieu_nai.html', {'form': form})
