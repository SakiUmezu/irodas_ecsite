# Generated by Django 3.2 on 2022-03-05 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fav_products',
            field=models.ManyToManyField(blank=True, to='app.Product'),
        ),
    ]
