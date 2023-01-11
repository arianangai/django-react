from django.db import models

class Form(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    jobtitle = models.CharField(max_length=200)
    centername = models.CharField(max_length=200)
    businessdesc = models.CharField(max_length=200)
    centerstatus = models.CharField(max_length=200)
    licensecap = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    comments = models.TextField()
    tnc = models.BooleanField(default=True)

    def _str_(self):
        return self.firstname
