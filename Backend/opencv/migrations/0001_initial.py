# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cattle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=20)),
                ('breed', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('horn_size', models.CharField(max_length=10)),
                ('cattle_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='cattle_fa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='cattle_face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='cattle_reg_appliction_req',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=20)),
                ('breed', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('horn_size', models.CharField(max_length=20)),
                ('cattle_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('uid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('total_no_claims', models.IntegerField()),
                ('total_no_false_claim', models.IntegerField()),
                ('total_no_approved_claims', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_register_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('uid', models.CharField(max_length=50)),
                ('aadhar', models.CharField(max_length=14)),
                ('password', models.CharField(max_length=225)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='opencv.user')),
            ],
        ),
        migrations.AddField(
            model_name='cattle_reg_appliction_req',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencv.user_register_request'),
        ),
        migrations.AddField(
            model_name='cattle_face',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencv.user'),
        ),
        migrations.AddField(
            model_name='cattle_fa',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencv.user'),
        ),
        migrations.AddField(
            model_name='cattle',
            name='fid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencv.cattle_fa'),
        ),
        migrations.AddField(
            model_name='cattle',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencv.user'),
        ),
    ]