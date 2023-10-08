# Generated by Django 4.2.5 on 2023-10-06 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leads',
            name='borthday',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='course',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='group',
        ),
        migrations.AlterField(
            model_name='leads',
            name='ledstype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.period'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('female', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('borthday', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.course')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.groups')),
            ],
        ),
    ]