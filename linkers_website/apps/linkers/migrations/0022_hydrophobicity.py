# Generated by Django 4.2.2 on 2023-08-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkers', '0021_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hydrophobicity',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('sequence', models.CharField(max_length=100)),
                ('acidic_very_hydrophobic', models.FloatField(default=0)),
                ('acidic_hydrophobic', models.FloatField(default=0)),
                ('acidic_neutral', models.FloatField(default=0)),
                ('acidic_hydrophilic', models.FloatField(default=0)),
                ('neutral_very_hydrophobic', models.FloatField(default=0)),
                ('neutral_hydrophobic', models.FloatField(default=0)),
                ('neutral_neutral', models.FloatField(default=0)),
                ('neutral_hydrophilic', models.FloatField(default=0)),
                ('gravy_score', models.FloatField(default=0)),
                ('acidic_img_data', models.TextField()),
                ('neutral_img_data', models.TextField()),
            ],
        ),
    ]
