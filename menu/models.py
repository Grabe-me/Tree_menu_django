from django.db import models


class MainMenu(models.Model):
    name = models.CharField('Пункт главного меню', max_length=50)
    parent = models.ForeignKey('self', parent_link=True, on_delete=models.PROTECT,
                               null=True, blank=True, related_name='children')


    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт главного меню'
        verbose_name_plural = 'Пункты  главного меню'
        ordering = ['name']


class AnotherMenu(models.Model):
    name = models.CharField('Пункт другого меню', max_length=50)
    parent = models.ForeignKey('self', parent_link=True, on_delete=models.PROTECT,
                               null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт другого меню'
        verbose_name_plural = 'Пункты другого меню'
        ordering = ['name']