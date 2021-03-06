# Generated by Django 3.0.3 on 2020-02-27 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('maker', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=1)),
                ('type', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('speed', models.SmallIntegerField()),
                ('ram', models.SmallIntegerField()),
                ('hd', models.FloatField()),
                ('cd', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('speed', models.SmallIntegerField()),
                ('ram', models.SmallIntegerField()),
                ('hd', models.FloatField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('screen', models.SmallIntegerField()),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.Product')),
            ],
        ),
    ]
