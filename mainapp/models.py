from django.db import models

# Create your models here.
class Cure(models.Model):
    name = models.CharField(max_length=50)
    pharmacies = models.ManyToManyField('Pharmacy', through='Place')
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Pharmacy(models.Model):
    name = models.CharField(max_length=50)
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True)
    cures = models.ManyToManyField(Cure,through='Place')
    def __str__(self):
        return self.name

class Place(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    cure = models.ForeignKey(Cure, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=3)
    def __str__(self):
        return self.pharmacy.name + '/' + self.cure.name + '(' + str(self.quantity) + ')'

