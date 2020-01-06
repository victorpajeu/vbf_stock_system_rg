from django.db import models


class Produto(models.Model):
    importado = models.BooleanField(default=False),
    ncm = models.CharField('NCM', max_length=100, unique=True),
    produto = models.CharField(max_length=200, unique=True),
    preco = models.DecimalField('preco', max_digits=7, decimal_places=2),
    estoque = models.IntegerField('estoque atual'),
    estoque_min = models.PositiveIntegerField('estoque minimo', default=0),

    def __str__(self):
        return self.produto.name
