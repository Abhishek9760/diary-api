# Generated by Django 2.2.10 on 2021-02-08 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='text',
            field=models.TextField(default='Enter Something', max_length=1000),
            preserve_default=False,
        ),
    ]