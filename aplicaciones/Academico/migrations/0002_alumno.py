# Generated by Django 4.2.5 on 2023-10-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('nota', models.PositiveSmallIntegerField()),
            ],
        ),
    ]