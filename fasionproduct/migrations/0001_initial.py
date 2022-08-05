# Generated by Django 4.0.6 on 2022-07-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('modl', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=2000)),
            ],
        ),
    ]
