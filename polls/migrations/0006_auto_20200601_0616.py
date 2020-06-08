# Generated by Django 2.2.4 on 2020-06-01 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200525_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.CharField(default=1, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.CharField(default=1, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('shortname', models.CharField(max_length=50)),
                ('dept', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('section', models.CharField(max_length=50)),
                ('sem', models.IntegerField(default=1)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='AttendenceClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.IntegerField(default=0)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Assign')),
            ],
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateField(default='01-06-2020')),
                ('attendenceclass', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.AttendenceClass')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Student')),
            ],
        ),
        migrations.CreateModel(
            name='AssignDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday')], max_length=50)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Assign')),
            ],
        ),
        migrations.AddField(
            model_name='assign',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Class'),
        ),
        migrations.AddField(
            model_name='assign',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Course'),
        ),
        migrations.AddField(
            model_name='assign',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='class_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Class'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='dept',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Dept'),
        ),
        migrations.AlterUniqueTogether(
            name='assign',
            unique_together={('course_id', 'class_id', 'teacher_id')},
        ),
    ]
