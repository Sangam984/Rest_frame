# Generated by Django 4.0.2 on 2023-09-15 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Grade_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.grade')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('Content', models.TextField()),
                ('sub_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.grade_sub')),
            ],
        ),
    ]
