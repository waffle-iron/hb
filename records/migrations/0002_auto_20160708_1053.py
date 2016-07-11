# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 10:53
from __future__ import unicode_literals

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='tags',
            field=bitfield.models.BitField((('books', 'Books'), ('cafe', 'Cafe'), ('clothes', 'Clothes'), ('fees', 'Fees'), ('food', 'Food'), ('fun', 'Fun'), ('gift', 'Gift'), ('health', 'Health'), ('hobby', 'Hobby'), ('household', 'Household'), ('hz', 'HZ'), ('internet', 'Internet'), ('lunch', 'Lunch'), ('managment_fee', 'Managment fee'), ('mobile', 'Mobile'), ('rent', 'Rent'), ('school', 'School'), ('sport', 'Sport'), ('tax', 'Tax'), ('technics', 'Technics'), ('to_save', 'To savings'), ('toys', 'Toys'), ('transport', 'Transport'), ('travel', 'Travel'), ('salary', 'Salary'), ('other', 'Other')), default=None),
        ),
    ]
