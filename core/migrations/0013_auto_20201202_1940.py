# Generated by Django 3.0.8 on 2020-12-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20201130_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userservice',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
