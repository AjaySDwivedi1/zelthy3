# Generated by Django 4.2.2 on 2023-08-04 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appauth', '0007_userrolemodel_temp_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50, null=True)),
                ('text', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('postalCode', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postalCode', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LandingPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestModel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestModel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('telecom', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ('unknown', 'Unknown')], default='unknown', max_length=10)),
                ('birthDate', models.DateField()),
                ('deceasedBoolean', models.BooleanField(default=False)),
                ('deceasedDateTime', models.DateTimeField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_models.address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FrameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.JSONField()),
                ('timestamp', models.DateField(null=True)),
                ('test', models.CharField(max_length=100, null=True)),
                ('many_test', models.ManyToManyField(to='appauth.userrolemodel')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appauth.userrolemodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]