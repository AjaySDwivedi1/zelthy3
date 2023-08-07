# Generated by Django 4.2.2 on 2023-08-06 05:58

from django.db import migrations, models
import django.db.models.deletion
import zelthy3.backend.apps.tenants.dynamic_models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appauth', '0007_userrolemodel_temp_field'),
        ('dynamic_models', '0004_framesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=255)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(blank=True, editable=False, max_length=255)),
                ('short_code', models.CharField(blank=True, max_length=25, verbose_name='Short Code of Program')),
                ('program_name', models.CharField(max_length=255, unique=True, verbose_name='Program Name')),
                ('description', models.TextField(blank=True, verbose_name='Program Description')),
                ('patient_eligibility', models.TextField(blank=True, max_length=2000)),
                ('program_eligibility', models.TextField(blank=True, max_length=2000)),
                ('extrafield1_char', models.CharField(blank=True, max_length=255, verbose_name='Extra Field1 Char')),
                ('extrafield2_char', models.CharField(blank=True, max_length=255, verbose_name='Extra Field2 Char')),
                ('extrafield3_char', models.CharField(blank=True, max_length=255, verbose_name='Extra Field3 Char')),
                ('extrafield1_boolean', models.BooleanField(default=False, verbose_name='Extra Field1 Boolean')),
                ('extrafield2_boolean', models.BooleanField(default=False, verbose_name='Extra Field2 Boolean')),
                ('extrafield3_boolean', models.BooleanField(default=False, verbose_name='Extra Field3 Boolean')),
                ('is_delivered_as_camp', models.BooleanField(default=False, verbose_name='Is the program delivered as camp')),
                ('program_delivered_through', models.CharField(blank=True, choices=[('hospital', 'Hospital'), ('doctor', 'Doctor')], max_length=50, verbose_name='Camp delivery mode')),
                ('jsonfield_extra1', models.JSONField(blank=True, null=True)),
                ('therapy_roles', zelthy3.backend.apps.tenants.dynamic_models.fields.ZManyToManyField(to='appauth.userrolemodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProgramApplicationValidator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artifact', models.CharField(max_length=255, verbose_name='Program Eligibility Artifact')),
                ('condition', models.TextField(blank=True, max_length=2000)),
                ('program', zelthy3.backend.apps.tenants.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validator', to='dynamic_models.programmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
