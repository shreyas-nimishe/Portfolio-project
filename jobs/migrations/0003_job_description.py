# Generated by Django 3.0.6 on 2020-05-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200524_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]