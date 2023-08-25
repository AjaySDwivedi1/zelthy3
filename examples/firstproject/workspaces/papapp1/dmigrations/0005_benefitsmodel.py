# Generated by Django 4.2.4 on 2023-08-25 10:18

from django.db import migrations, models
import django.db.models.deletion
import zelthy.apps.dynamic_models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0004_programmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BenefitsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_code', models.CharField(blank=True, max_length=25, verbose_name='Short Code of Benefit')),
                ('label', models.CharField(max_length=255, verbose_name='Label')),
                ('benefit_type', models.CharField(blank=True, choices=[('drug', 'Drug Benefit'), ('others', 'Others')], max_length=50, verbose_name='Benefit Type')),
                ('benefit_category', models.CharField(blank=True, choices=[('free', 'Free'), ('prepaid', 'Prepaid'), ('cod', 'Cash on Delivery')], max_length=50, verbose_name='Benefit Category')),
                ('item_choice_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for Choosing')),
                ('generate_order_condition', models.TextField(blank=True, max_length=4000, verbose_name='Condition for Generating Order')),
                ('update_credit_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for updating credit')),
                ('order_dispense_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order dispense')),
                ('order_close_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order close')),
                ('order_extrastatus_1_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 1')),
                ('order_extrastatus_2_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 2')),
                ('order_extrastatus_3_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 3')),
                ('order_extrastatus_4_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 4')),
                ('order_extrastatus_5_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 5')),
                ('order_extrastatus_6_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 6')),
                ('order_extrastatus_7_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 7')),
                ('order_extrastatus_8_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 8')),
                ('order_extrastatus_9_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 9')),
                ('order_extrastatus_10_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 10')),
                ('order_extrastatus_11_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 11')),
                ('order_extrastatus_12_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Extra Status 12')),
                ('order_return_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order return')),
                ('order_cancel_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order cancel')),
                ('order_scan_in_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Scan In')),
                ('order_scan_out_condition', models.TextField(blank=True, max_length=2000, verbose_name='Condition for order Scan Out')),
                ('priority', models.IntegerField(default=0, verbose_name='Benefit Priority Order')),
                ('extrafield1_text', models.TextField(blank=True, verbose_name='ExtraField1 Text')),
                ('extrafield2_text', models.TextField(blank=True, verbose_name='ExtraField2 Text')),
                ('extrafield1_char', models.CharField(blank=True, max_length=255, verbose_name='ExtraField1 Char')),
                ('extrafield2_char', models.CharField(blank=True, max_length=255, verbose_name='ExtraField2 Char')),
                ('program', zelthy.apps.dynamic_models.fields.ZForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='benefits', to='dynamic_models.programmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
