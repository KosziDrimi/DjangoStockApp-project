# Generated by Django 3.2.5 on 2021-07-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_2', '0002_auto_20210719_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='Cena_KGH',
            new_name='Cena',
        ),
        migrations.RemoveField(
            model_name='price',
            name='Cena_PKN',
        ),
        migrations.RemoveField(
            model_name='price',
            name='Cena_SEN',
        ),
        migrations.AddField(
            model_name='price',
            name='Nazwa_spółki',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
