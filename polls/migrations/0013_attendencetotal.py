# Generated by Django 2.2.4 on 2020-06-03 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20200601_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendenceTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
