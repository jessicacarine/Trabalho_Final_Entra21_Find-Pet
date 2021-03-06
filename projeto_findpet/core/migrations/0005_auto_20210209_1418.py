# Generated by Django 3.1.5 on 2021-02-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210208_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='pet',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='district',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterModelTable(
            name='eu_vi',
            table='core_eu_vi',
        ),
    ]
