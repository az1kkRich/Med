# Generated by Django 4.0.4 on 2022-07-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=250)),
                ('ixtisosi', models.CharField(max_length=50)),
                ('summa', models.CharField(max_length=50)),
            ],
        ),
    ]
