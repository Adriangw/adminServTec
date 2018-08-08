# Generated by Django 2.0.7 on 2018-08-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=30)),
                ('secretaria', models.PositiveIntegerField(choices=[(1, 'Seleccione La Secretaria que Corresponde'), (2, 'SECRETARIA DE HACIENDA'), (3, 'SECRETARIA DE GOBIERNO'), (4, 'SECRETARIA DE FAMILIA'), (5, 'SECRETARIA DE CULTURA'), (6, 'SECRETARIA DE PLANIFICACION')])),
                ('sector', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=30)),
                ('archivo', models.FileField(upload_to='documents')),
                ('so', models.CharField(max_length=100)),
                ('cpu', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
                ('madre', models.CharField(max_length=100)),
                ('graf', models.CharField(max_length=100)),
                ('disk', models.CharField(max_length=100)),
                ('optic', models.CharField(max_length=100)),
                ('audio', models.CharField(max_length=100)),
                ('mac', models.TextField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=50)),
            ],
        ),
    ]
