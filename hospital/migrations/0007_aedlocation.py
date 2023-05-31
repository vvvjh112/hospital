# Generated by Django 4.1.2 on 2022-10-24 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_alter_normalh_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='aedLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aed_id', models.IntegerField()),
                ('설치기관명', models.TextField(blank=True, null=True)),
                ('설치장소', models.TextField(blank=True, null=True)),
                ('관리자', models.TextField(blank=True, null=True)),
                ('관리자연락처', models.TextField(blank=True, null=True)),
                ('경도', models.TextField(blank=True, null=True)),
                ('위도', models.TextField(blank=True, null=True)),
                ('우편번호', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'AED',
                'managed': False,
            },
        ),
    ]