# Generated by Django 4.0.3 on 2022-09-25 18:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('event_home_url', models.URLField()),
                ('event_registration_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('goal_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('result_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events_app.event')),
            ],
        ),
    ]