# Generated by Django 2.1 on 2018-10-12 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Ciudad', models.PositiveSmallIntegerField()),
                ('Descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Region', models.PositiveSmallIntegerField()),
                ('Descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Tipo_Vivienda', models.PositiveSmallIntegerField()),
                ('Descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correo', models.CharField(max_length=40)),
                ('Run', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Fecha_Nacimineto', models.DateField()),
                ('Fono', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Vivienda', models.PositiveSmallIntegerField()),
                ('Descripcion', models.CharField(max_length=20)),
                ('Tipo_Vivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formulario.Tipo_Vivienda')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='Vivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formulario.Vivienda'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='Region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Formulario.Region'),
        ),
    ]
