from django.db import models

# Create your models here.
class principal(models.Model):
    pname=models.CharField(max_length=25)
    pusername=models.CharField(max_length=20)
    ppassword=models.CharField(max_length=20)
    pid=models.CharField(primary_key=True, max_length=20)
    pemail=models.EmailField(max_length=35)
    pmob=models.IntegerField()

    def __str__(self):
        return self.pname.upper()

class teacher(models.Model):
    tname=models.CharField(max_length=20)
    tusername=models.CharField(max_length=20)
    tpassword=models.CharField(max_length=20)
    tgender=models.CharField(max_length=20)
    tdob=models.DateField()
    tmob=models.IntegerField()
    tage=models.IntegerField()
    tsub=models.CharField(max_length=20)

    def __str__(self):
        return self.tname.upper()

class student(models.Model):
    sname=models.CharField(max_length=20)
    susername=models.CharField(max_length=20)
    spassword=models.CharField(max_length=20)
    sgender=models.CharField(max_length=20)
    sdob=models.DateField()
    smob=models.IntegerField()
    sage=models.IntegerField()
    sclass=models.IntegerField()

    def __str__(self):
        return self.sname.upper()

class notice(models.Model):
    date=models.DateField()
    slno=models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=500)
    def __str__(self):
        return self.title