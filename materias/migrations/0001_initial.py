# Generated by Django 2.1.3 on 2018-11-19 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=200)),
                ('seccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='grado',
            name='materias',
            field=models.ManyToManyField(through='materias.Detalle', to='materias.Materia'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materias.Grado'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materias.Materia'),
        ),
    ]
