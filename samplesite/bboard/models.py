from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='goods')
    content = models.TextField(null=True, blank=True, verbose_name='description')
    price = models.FloatField(null=True, blank=True, verbose_name='price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='published')

    class Meta:
        verbose_name = 'Annoncement'
        verbose_name_plural = 'Annoncement'
        ordering = ['-published']
