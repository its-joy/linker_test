# Generated by Django 4.2.2 on 2023-08-08 19:33

from django.db import migrations, models
import linkers_website.apps.testapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flexibility',
            fields=[
                ('id', models.CharField(default='1', max_length=15, primary_key=True, serialize=False)),
                ('Sequence', models.CharField(max_length=100)),
                ('backbone', models.CharField()),
                ('average_flexibility', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TestLinker',
            fields=[
                ('id', models.CharField(default=linkers_website.apps.testapp.models.id_generator, editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('pdb_id', models.CharField(default=None, max_length=15)),
                ('length', models.IntegerField(default=0)),
                ('aasequence', models.CharField(max_length=255)),
                ('Source', models.CharField(max_length=350)),
                ('Reference', models.CharField(default=None, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.CharField(default=linkers_website.apps.testapp.models.id_generator, editable=False, primary_key=True, serialize=False, unique=True)),
                ('aasequence', models.CharField(max_length=255)),
                ('Origin', models.CharField(max_length=225)),
            ],
        ),
    ]