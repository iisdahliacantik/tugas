from django.contrib import admin
from django.urls import path
from administrasi.views import administrasi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrasi/',administrasi),
]
