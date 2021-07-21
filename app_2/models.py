from django.db import models


class Price(models.Model):
    Data = models.DateField() 
    Cena_KGH = models.FloatField()
    Cena_PKN = models.FloatField()
    Cena_SEN = models.FloatField()

    def __str__(self):
        return f'<{self.Data}, {self.Cena_KGH}, {self.Cena_PKN}, {self.Cena_SEN}>'
