from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=45)
    address = models.CharField(max_length=200)
    workPlace = models.CharField(max_length=45)
    sex = models.CharField(max_length=25)
    
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.name, self.lastName, self.email)

class position(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)
