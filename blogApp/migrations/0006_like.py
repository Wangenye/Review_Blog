# Generated by Django 3.1 on 2020-10-31 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_auto_20201031_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to='blogApp.Blog')),
            ],
        ),
    ]
