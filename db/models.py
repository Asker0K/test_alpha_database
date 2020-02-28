from django.db import models


class Product(models.Model):
    maker = models.CharField(max_length=10)
    model = models.CharField(max_length=50, primary_key=True)
    type = models.CharField(max_length=50)

class Laptop(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey("Product", null=True, on_delete=models.SET_NULL, related_name="laptop")
    speed = models.SmallIntegerField()
    ram = models.SmallIntegerField()
    hd = models.FloatField()
    price = models.DecimalField(null=True, decimal_places=2,max_digits=5)
    screen = models.SmallIntegerField()


class Pc(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey("Product", null=True, on_delete=models.SET_NULL, related_name="pc")
    speed = models.SmallIntegerField()
    ram = models.SmallIntegerField()
    hd = models.FloatField()
    cd = models.CharField(max_length=10)
    price =models.DecimalField(null=True, decimal_places=2,max_digits=5)


class Printer(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey("Product", null=True, on_delete=models.SET_NULL, related_name="printer")
    color = models.CharField(max_length=1)
    type = models.CharField(max_length=10)
    price = models.DecimalField(null=True, decimal_places=2,max_digits=5)