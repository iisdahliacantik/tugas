from django.shortcuts import render

def administrasi(request):
    judul = ["pembayaran", "Check Out", "Bayar"]
    pembeli = "Iis Dayanti"

    konteks = {
        'title': judul,
        'pembeli' : pembeli,
    }
    return render(request, 'administrasi.html', konteks)
