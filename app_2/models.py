from django.db import models


class Price(models.Model):
    Data = models.DateField() 
    Nazwa_spółki = models.CharField(max_length = 10)
    Cena = models.FloatField()


    def __str__(self):
        return f'<{self.Data}, {self.Nazwa_spółki}, {self.Cena}>'
