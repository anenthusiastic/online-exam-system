# Generated by Django 2.2.13 on 2021-02-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20210224_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='optionE',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='OptionE'),
        ),
    ]
