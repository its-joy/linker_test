# Generated by Django 4.2.2 on 2023-08-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkers', '0015_delete_empmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('length', models.IntegerField(default=0)),
                ('aasequence', models.CharField(max_length=255)),
                ('Origin', models.CharField(max_length=225)),
            ],
        ),
    ]