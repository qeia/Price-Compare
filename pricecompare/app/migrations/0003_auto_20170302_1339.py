# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170302_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='amazon_price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='gamestop_price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='target_price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='walmart_price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
