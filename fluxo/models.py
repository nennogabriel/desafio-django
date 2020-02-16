from django.db import models

class Caixa(models.Model):
    nome = models.CharField(max_length=200)
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fechado = models.BooleanField(default=False)
    def status(self):
        return self.fechado and "fechado" or "aberto"
    def __str__(self):
        return "%s - %s com %s" % (self.status(), self.nome, self.valor_inicial)

class MeioDePagamento(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Mesa(models.Model):
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fechado = models.BooleanField(default=False)
    def status(self):
        return self.fechado and "fechado" or "aberto"
    def __str__(self):
        return "%s - %s" % (self.referencia, self.status())

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return "%s :  $%s" % (self.nome, self.valor)

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    def __str__(self):
        return "%s x %s para %s" % (self.quantidade, self.produto, self.mesa)

class Pagamento(models.Model):
    nome = models.CharField(max_length=200)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    meio_de_pagamento = models.ForeignKey(MeioDePagamento, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return "pago %s com %s para %s por %s" % (self.valor, self.meio_de_pagamento, self.mesa, self.nome)
