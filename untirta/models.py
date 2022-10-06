from django.db import models

# Create your models here.
class Dosen(models.Model) :
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    tanggal_lahir = models.CharField(max_length=50)
    foto = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)
    alamat_rumah = models.CharField(max_length=50)

    def str(self):
        return self.nama

class Staf(models.Model) :
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    tanggal_lahir= models.CharField(max_length=50)
    foto = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    alamat_rumah = models.CharField(max_length=50)

    def str(self):
        return self.nama
    
class Mahasiswa(models.Model) :
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    tanggal_lahir= models.CharField(max_length=50)
    foto = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)

    def str(self):
        return self.nama