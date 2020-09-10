# Generated by Django 3.1 on 2020-09-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nairobi_hospitals_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointcloudFormats',
            fields=[
                ('pcid', models.IntegerField(primary_key=True, serialize=False)),
                ('srid', models.IntegerField(blank=True, null=True)),
                ('schema', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pointcloud_formats',
            },
        ),
        migrations.AddField(
            model_name='nairobihealthfacilities',
            name='distance',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]