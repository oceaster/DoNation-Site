# Generated by Django 2.2 on 2021-02-05 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.TextField(editable=False)),
                ('pledge', models.TextField()),
                ('save_co2', models.FloatField(default=0.0)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
