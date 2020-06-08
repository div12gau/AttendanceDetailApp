# Generated by Django 2.2.4 on 2020-06-01 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200601_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Dept'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='id',
            field=models.CharField(max_length=50, primary_key='True', serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Dept'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]