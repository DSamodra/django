from django.contrib import admin
from django.urls import path
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView

# require to show images
from django.conf.urls.static import static

#require for deployment
from django.views.static import serve
from django.conf.urls import url

# basic routing to apps in view.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku, name='buku'),
    path('penerbit/', penerbit, name='penerbit'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),

    # path with parameter and name
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name='hapus_buku'),

    # path url with login view
    # login view wil direct in folder template registration login.html
    path('masuk/', LoginView.as_view(), name='masuk'),

    # logout and redirect to login page
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),

    # signup account
    path('signup/', signup, name='signup'),

    # export
    path('export/xls/', export_xls, name='export_xls'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

# require to show book in perpustakaan
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
