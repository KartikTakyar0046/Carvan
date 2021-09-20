# Generated by Django 3.1.7 on 2021-03-05 15:17

import autoslug.fields
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20210304_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='caravan',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]