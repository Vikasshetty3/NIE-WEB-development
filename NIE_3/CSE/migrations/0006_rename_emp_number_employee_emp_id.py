# Generated by Django 5.1.1 on 2024-09-13 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0005_rename_emp_id_employee_emp_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emp_number',
            new_name='emp_id',
        ),
    ]
