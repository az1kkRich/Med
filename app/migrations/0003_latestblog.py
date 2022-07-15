# Generated by Django 4.0.4 on 2022-06-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_services_servicesimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=250)),
                ('time', models.DateTimeField()),
                ('img', models.ImageField(upload_to='BlogImg')),
            ],
        ),
    ]
