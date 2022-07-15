# Generated by Django 4.0.4 on 2022-06-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_latestblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='BlogImg')),
            ],
        ),
    ]
