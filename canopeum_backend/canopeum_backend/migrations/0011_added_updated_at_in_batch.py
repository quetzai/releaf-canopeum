# Generated by Django 5.0.3 on 2024-04-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canopeum_backend', '0010_rename_linkedin_link_contact_linkedin_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='linkedIn_link',
            new_name='linkedin_link',
        ),
        migrations.AddField(
            model_name='batch',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]