# Generated by Django 4.2.4 on 2023-09-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyramidWebConnector', '0002_alter_categorymapping_id_alter_consolemessage_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='erp_server_port',
            new_name='ftp_folder',
        ),
        migrations.RenameField(
            model_name='useranswer',
            old_name='woo_consumer_secret',
            new_name='ftp_password',
        ),
        migrations.AddField(
            model_name='useranswer',
            name='ftp_server',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useranswer',
            name='ftp_username',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
