# Generated by Django 3.1 on 2020-10-31 21:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0008_auto_20201031_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
