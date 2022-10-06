from django.db import models

# Create your models here.
class dosen(models.Model):
    NIP = models.IntegerField(null=True)
    nama = models.CharField(max_length=50)
    tl = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
     def __str__(self):
        return self.nama

class tendik(models.Model):
    NIP = models.IntegerField(null=True)
    nama = models.CharField(max_length=50)
    tl = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
     def __str__(self):
        return self.nama

class mahasiswa(models.Model):
    NIM = models.IntegerField(null=True)
    nama = models.CharField(max_length=50)
    tl = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)

    def __str__(self):
        return self.nama