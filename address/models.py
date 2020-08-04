from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class City(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100, help_text=_('city name'), unique=True,
                            db_index=True)
    population = models.IntegerField(verbose_name=_('population'), max_length=100, default=0)

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        ordering = ['-population']

    def __str__(self):
        return f"{self.name} ({self.population})"


class Address(models.Model):
    country = models.CharField(verbose_name=_('country'), max_length=100,
                               help_text=_('country'))
    street = models.CharField(verbose_name=_('street'), max_length=100,
                              help_text=_('street'))
    city = models.ForeignKey(City, verbose_name=_('city'), help_text=_('city'), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return f"{self.city} {self.street}"

