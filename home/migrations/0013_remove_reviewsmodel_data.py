# Generated by Django 4.0.5 on 2022-06-20 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_reviewsmodel_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewsmodel',
            name='data',
        ),
    ]
