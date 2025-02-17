# Generated by Django 3.2.9 on 2021-11-26 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('name', models.CharField(db_index=True, max_length=1024)),
                ('package_url', models.CharField(blank=True, db_index=True, max_length=1024, null=True)),
                ('metadata', models.JSONField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('package_url', models.CharField(blank=True, db_index=True, max_length=1024, null=True)),
                ('metadata', models.JSONField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triage.project')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TriageRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(choices=[('FN', 'On New Finding'), ('FM', 'On Modified Finding')], default='FN', max_length=2)),
                ('condition', models.TextField(blank=True, max_length=2048, null=True)),
                ('action', models.TextField(blank=True, max_length=2048, null=True)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('priority', models.PositiveSmallIntegerField(default=1000)),
                ('type', models.CharField(choices=[('PY', 'Python Function')], default='PY', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=128)),
                ('version', models.CharField(blank=True, max_length=64)),
                ('type', models.CharField(choices=[('NS', 'Not Specified'), ('MA', 'Manual'), ('SA', 'Static Analysis'), ('OT', 'Other')], default='NS', max_length=2)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('artifact_uuid', models.UUIDField(blank=True, editable=False, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triage.projectversion')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triage.tool')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Finding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=1024)),
                ('file_path', models.CharField(max_length=2048)),
                ('file_line', models.PositiveIntegerField(blank=True, null=True)),
                ('impact_usage', models.PositiveBigIntegerField(blank=True, null=True)),
                ('impact_context', models.PositiveBigIntegerField(blank=True, null=True)),
                ('analyst_impact', models.PositiveBigIntegerField(blank=True, null=True)),
                ('confidence', models.CharField(choices=[('NS', 'Not Specified'), ('VL', 'Very Low'), ('L', 'Low'), ('M', 'Medium'), ('H', 'High'), ('VH', 'Very High')], default='NS', max_length=2)),
                ('severity_level', models.CharField(choices=[('NS', 'Not Specified'), ('NO', 'None'), ('IN', 'Informational'), ('VL', 'Very Low'), ('L', 'Low'), ('M', 'Medium'), ('H', 'High'), ('VH', 'Very High')], default='NS', max_length=2)),
                ('analyst_severity_level', models.CharField(choices=[('NS', 'Not Specified'), ('NO', 'None'), ('IN', 'Informational'), ('VL', 'Very Low'), ('L', 'Low'), ('M', 'Medium'), ('H', 'High'), ('VH', 'Very High')], default='NS', max_length=2)),
                ('state', models.CharField(choices=[('N', 'New'), ('A', 'Active'), ('R', 'Resolved'), ('D', 'Deleted'), ('CL', 'Closed'), ('NS', 'Not Specified')], default='N', max_length=2)),
                ('assigned_dt', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('scan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triage.scan')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('definition', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('priority', models.PositiveSmallIntegerField(default=1000)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='triage.project')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('state', models.CharField(choices=[('N', 'New'), ('R', 'Reported'), ('A', 'Active'), ('RS', 'Resolved'), ('D', 'Deleted'), ('CL', 'Closed'), ('NS', 'Not Specified')], default='N', max_length=2)),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField(blank=True, null=True)),
                ('assigned_dt', models.DateTimeField(auto_now_add=True)),
                ('reported_to', models.CharField(blank=True, max_length=2048, null=True)),
                ('reporting_partner', models.CharField(blank=True, choices=[('N', 'None'), ('GS', 'GitHub Security Lab'), ('CT', 'CERT'), ('MS', 'MSRC'), ('NS', 'Not Specified')], default='NS', max_length=2, null=True)),
                ('report_foreign_reference', models.CharField(blank=True, max_length=1024, null=True)),
                ('resolved_target_dt', models.DateTimeField(blank=True, null=True)),
                ('resolved_dt', models.DateTimeField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_cases', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('findings', models.ManyToManyField(related_name='cases', to='triage.Finding')),
                ('notes', models.ManyToManyField(related_name='cases', to='triage.Note')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
