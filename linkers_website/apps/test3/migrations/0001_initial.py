# Generated by Django 4.2.2 on 2023-08-08 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linker',
            fields=[
                ('id', models.CharField(default='1', max_length=15, primary_key=True, serialize=False)),
                ('pdb_id', models.CharField(default=None, max_length=15)),
                ('length', models.IntegerField(default=0)),
                ('aasequence', models.CharField(max_length=255)),
                ('Source', models.CharField(max_length=350)),
                ('Reference', models.CharField(default=None, max_length=400)),
            ],
        ),
    ]
