from django.contrib import admin
from django.urls import path, include

from DIVA import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DIVA.urls')),  # Tích hợp URL của ứng dụng diva
    path('dang-ky/', views.dang_ky),
    path('khieu-nai/', views.khieu_nai)
]
