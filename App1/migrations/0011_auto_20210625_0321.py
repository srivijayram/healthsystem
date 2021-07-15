# Generated by Django 3.2.3 on 2021-06-24 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0010_documents_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('receiver', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='')),
                ('transactiontime', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Documents',
        ),
    ]
