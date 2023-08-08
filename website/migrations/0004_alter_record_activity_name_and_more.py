# Generated by Django 4.2.3 on 2023-08-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_record_activity_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='activity_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='activity_type',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='affilation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='county',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='fee',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='pass_fail',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='position',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='section',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='sponsor',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='year',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='zipcode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]