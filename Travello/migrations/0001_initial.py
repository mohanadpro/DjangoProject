# Generated by Django 3.0.5 on 2020-04-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

# steps to migrate database
# 1. create class model as a Model
# 2. determine the fields as a Model
# 3. determine the database configuration in the setting file
#     a. determine the type of the database in the DATABASES section
#     b. determine the name of the application that has the models in the INSTALLED_APPS section
# 4. create database in the postgres 
# 5. if you have a field with image type you should install pillow library 
# 6. excute migrate command "python manage.py makemigration" which create migration file
# 7. excute migrate command "python manage.py sqlmigrate 'databasename' 'migrationfilename'" that convert the migration to Query
# 8. excute migrate command "python manage.py migrate" which create the tables or update the database

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]