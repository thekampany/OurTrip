# Generated by Django 3.2.19 on 2024-02-02 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badgename', models.CharField(default='badgename', max_length=100)),
                ('badge', models.URLField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Our Trip', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tripname', models.CharField(default='Our Trip', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tripper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tripper', models.CharField(max_length=100)),
                ('badges', models.ManyToManyField(to='ourtripapp.Badge')),
            ],
        ),
        migrations.CreateModel(
            name='DayProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tripdate', models.DateField(verbose_name='date')),
                ('dayprogramnumber', models.IntegerField()),
                ('dayprogram', models.CharField(max_length=100)),
                ('bookedactivities', models.TextField(null=True)),
                ('possibleactivities', models.TextField(null=True)),
                ('documentsneeded', models.TextField(null=True)),
                ('task', models.TextField(null=True)),
                ('actionitems', models.CharField(max_length=400, null=True)),
                ('part_of_trip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ourtripapp.trip')),
            ],
        ),
    ]
