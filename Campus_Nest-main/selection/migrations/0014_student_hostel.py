# Generated by Django 4.2.6 on 2023-10-29 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0013_student_due_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hostel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='selection.hostel'),
        ),
    ]
