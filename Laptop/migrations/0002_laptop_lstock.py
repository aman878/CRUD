# Generated by Django 3.2 on 2021-05-02 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laptop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='lstock',
            field=models.CharField(default='No', max_length=3),
        ),
    ]
