# Generated by Django 4.2.2 on 2023-06-09 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flotilla', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='modelo',
            name='Marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='flotilla.marca'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='Notas',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flotilla.area')),
            ],
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=200)),
                ('Departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flotilla.departamento')),
            ],
        ),
    ]
