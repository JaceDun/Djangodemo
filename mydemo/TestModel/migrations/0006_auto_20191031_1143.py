# Generated by Django 2.2.5 on 2019-10-31 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0005_contact_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Stud',
        ),
    ]
