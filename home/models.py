from django.db import models


class CountryModel(models.Model):
    d_name = models.CharField(max_length=30)
    president = models.CharField(max_length=30)
    aholi_soni = models.PositiveIntegerField()
    mustaqilligi = models.PositiveIntegerField()

    def __str__(self):
        return self.d_name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Poytaxt(models.Model):
    p_name = models.CharField(max_length=100)
    davlat = models.OneToOneField(CountryModel, on_delete=models.RESTRICT)

    def __str__(self):
        return self.p_name

    class Meta:
        verbose_name = 'Poytaxt'
        verbose_name_plural = 'Poytaxtlar'
