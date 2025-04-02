# Generated by Django 5.1.7 on 2025-04-02 15:27

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='action',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='actiondata',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actiondata',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='eventdata',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventdata',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='property',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='schema',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schema',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=40, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('ip_addr', models.CharField(blank=True, max_length=36, null=True)),
                ('online', models.BooleanField(default=False)),
                ('port', models.CharField(blank=True, max_length=5, null=True)),
                ('location', models.JSONField()),
                ('description', models.TextField()),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('parent_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='core.device')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceShadow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.JSONField()),
                ('desired_state', models.JSONField()),
                ('reported_state', models.JSONField()),
                ('version', models.IntegerField(default=0)),
                ('last_updated_dt', models.DateTimeField(auto_now=True)),
                ('creatd_dt', models.DateTimeField(auto_now_add=True)),
                ('online', models.BooleanField(default=False)),
                ('last_connected_at', models.DateTimeField()),
                ('lock_status', models.CharField(choices=[('LOCKED', 'locked'), ('UNLOCK', 'unlock')], max_length=6)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shadow', to='core.device')),
                ('last_updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=40, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('product_type', models.CharField(choices=[('GATEWAY_DEVICE', 'gateway'), ('GATEWAY_SUB_DEVICE', 'sub'), ('DIRECT_DEVICE', 'direct')], max_length=18)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.schema')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]
