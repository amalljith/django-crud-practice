# Generated by Django 5.0.4 on 2024-08-24 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broapp', '0003_de_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='de',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
