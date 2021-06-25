from django.shortcuts import render, redirect, HttpResponse
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages

# system for login first then you can use the feature
from django.contrib.auth.decorators import login_required
from django.conf import settings

# system to make account
from django.contrib.auth.forms import UserCreationForm

# import for export data
from perpustakaan.resource import BukuResource

# export database to excel
def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    # doenload file was exported
    response['Content-Disposition'] = 'attachment; filename = "laporan database.xls"'
    return response

#routing for login 
@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah dibuat")
            return redirect('signup')
        else :
            messages.error(request, "Akun tidak bisa dibuat")
            return redirect('signup')
    else :
        form = UserCreationForm()
        konteks = {
            'form' : form,
        }
    return render(request, 'signup.html', konteks)



# views for directing databse and routing

#routing for login 
@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    # subtitusi variable passing
    judul = "Belajar Django"
    list_judul = ['Belajar django', 'belajar python', 'ena ena']

    konteks1 = {
        'title': judul,
        'penulis': 'samodra',
        'list': list_judul
    }

    # ORM with if caluse filter
    # book = Buku.objects.filter(jumlah=100)

    # ORM with if caluse foreign key (inner join)
    # books = Buku.objects.filter(kelompok_id__nama='Produktif')

    # ORM with if caluse foreign key (inner join) with limit
    # books = Buku.objects.filter(kelompok_id__nama='Produktif')[:3]

    # ORM get all data from database
    books = Buku.objects.all()
    konteks = {
        'books': books,
    }

    return render(request, 'buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):

    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.success(request, "Data berhasil di hapus")
    return redirect('buku')

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):

    # orm to get data by id
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'

    if request.POST:
        #get all daata buku
        form = FormBuku(request.POST, request.FILES, instance = buku)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbaharui')
            return redirect('ubah_buku', id_buku = id_buku)

    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form': form,
            'buku': buku,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):

    # if there a post method on this request
    if request.POST:
        # get the form data to form
        # form = FormBuku(request.POST)
        
        #get data with request files
        form = FormBuku(request.POST, request.FILES)
        # checking is valid or not
        if form.is_valid():
            form.save()
            form = FormBuku()

            # sucess notification
            pesan = 'Data berhasil tersimpan'

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
    else:
        form = FormBuku()
        konteks = {
            'form': form,
        }
        return render(request, 'tambah-buku.html', konteks)
