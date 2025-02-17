# Generated by Django 4.0 on 2022-01-02 04:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0022_wikiarticle_alter_note_options_wikiarticlerevision_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wikiarticlerevision',
            old_name='parent',
            new_name='article',
        ),
        migrations.AddField(
            model_name='wikiarticlerevision',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
