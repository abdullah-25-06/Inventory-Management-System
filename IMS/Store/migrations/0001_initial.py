# Generated by Django 4.1.4 on 2023-04-13 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_name', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50)),
                ('quantity', models.IntegerField()),
                ('b_cost', models.BigIntegerField()),
                ('sell', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('s_id', models.IntegerField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=35, null=True)),
            ],
            options={
                'db_table': 'supplier',
                'managed': False,
            },
        ),
    ]