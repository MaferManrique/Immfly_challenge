# Generated by Django 4.2 on 2023-04-19 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='parent_channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subchannels', to='api.channel'),
        ),
        migrations.AlterField(
            model_name='content',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='api.channel'),
        ),
    ]
