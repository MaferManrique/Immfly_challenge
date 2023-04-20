# Generated by Django 4.2 on 2023-04-20 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_channel_parent_channel_alter_content_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='file',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.content'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metadata', to='api.content'),
        ),
    ]