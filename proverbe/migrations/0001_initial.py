# Generated by Django 4.2 on 2023-04-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proverbe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_ar', models.CharField(max_length=1000)),
                ('version_fra', models.CharField(max_length=1000)),
                ('explication', models.CharField(max_length=1000)),
            ],
        ),
    ]