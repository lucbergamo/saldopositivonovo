from django.db import models

class Gastos(models.Model):
    TIPOS = [
        ('Mercado', 'Mercado'),
        ('Farmácia', 'Farmácia'),
        ('Combustível', 'Combustível'),
        ('Casa', 'Casa'),
    ]
    nome = models.CharField('Nome do Gasto',max_length=100)
    preco = models.DecimalField('Preço',decimal_places=2, max_digits=10)
    data = models.DateField('Data de Gasto')
    criacao = models.DateTimeField(auto_now_add=True)
    criadoPor = models.CharField('Criado por',max_length=100)
    tipo = models.CharField('Tipo de Gasto',choices=TIPOS,max_length=50, default='Mercado')


