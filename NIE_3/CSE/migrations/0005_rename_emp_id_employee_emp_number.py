# Generated by Django 5.1.1 on 2024-09-13 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0004_rename_emp_number_employee_emp_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emp_id',
            new_name='emp_number',
        ),
    ]
