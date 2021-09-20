# Generated by Django 3.1.7 on 2021-03-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_auto_20210315_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='forum',
            name='description',
            field=models.CharField(blank=True, max_length=511),
        ),
        migrations.AlterField(
            model_name='stop',
            name='status',
            field=models.CharField(choices=[('decided', 'Decided'), ('tentative', 'Tentative'), ('proposal', 'Proposal')], default='proposal', max_length=15),
        ),
    ]