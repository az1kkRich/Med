# Generated by Django 4.0.4 on 2022-07-14 13:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_member_facebook_alter_member_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
