# Generated by Django 2.0.2 on 2018-03-02 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewlist', '0004_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewlist.Country'),
        ),
    ]
