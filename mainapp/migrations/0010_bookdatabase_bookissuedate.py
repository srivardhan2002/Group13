# Generated by Django 3.2 on 2021-11-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_bookdatabase_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdatabase',
            name='BookIssuedate',
            field=models.DateTimeField(null=True),
        ),
    ]
