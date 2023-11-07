# Generated by Django 4.2.6 on 2023-11-06 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0025_remove_complaint_created_at_remove_complaint_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Submitted', 'Submitted'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Submitted', max_length=20),
        ),
    ]