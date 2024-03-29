# Generated by Django 4.2.4 on 2023-08-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights3', '0005_delete_plane'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=30)),
                ('last', models.CharField(max_length=30)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights3.flight')),
            ],
        ),
    ]
