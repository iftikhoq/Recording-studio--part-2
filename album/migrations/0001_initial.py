# Generated by Django 5.1.5 on 2025-01-21 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')])),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musician.musician')),
            ],
        ),
    ]
