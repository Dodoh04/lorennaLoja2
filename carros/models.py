from django.db import models


class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=150)
    placa = models.CharField(max_length=10, unique=True, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    km = models.PositiveIntegerField(verbose_name='Quilometragem')
    cor = models.CharField(max_length=50, verbose_name='Cor', blank=True)
    combustivel = models.CharField(max_length=50, verbose_name='Combustível', blank=True)
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    preco = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Preço')

    class Meta:
        ordering = ['-data_cadastro']
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.marca} {self.modelo}'


class CarroImagem(models.Model):
    carro = models.ForeignKey(
        Carro,
        on_delete=models.CASCADE,
        related_name='imagens'
    )
    imagem = models.ImageField(upload_to='carros/')
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Imagem do Carro'
        verbose_name_plural = 'Imagens dos Carros'

    def __str__(self):
        return f"Imagem de {self.carro.marca} {self.carro.modelo}"


class Lead(models.Model):
    carro = models.ForeignKey(
        Carro,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='leads'
    )
    telefone = models.CharField(max_length=30)
    origem = models.CharField(max_length=100, default='Site')
    data_lead = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.telefone} - {self.origem}"


class Venda(models.Model):
    carro = models.ForeignKey(
        Carro,
        on_delete=models.PROTECT,
        related_name='vendas'
    )
    cliente = models.CharField(max_length=200)
    valor_venda = models.DecimalField(max_digits=12, decimal_places=2)
    data_venda = models.DateField(auto_now_add=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cliente} - {self.carro}"
