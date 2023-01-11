# Generated by Django 4.1.5 on 2023-01-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('jobtitle', models.CharField(max_length=200)),
                ('centername', models.CharField(max_length=200)),
                ('businessdesc', models.CharField(max_length=200)),
                ('centerstatus', models.CharField(max_length=200)),
                ('licensecap', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
