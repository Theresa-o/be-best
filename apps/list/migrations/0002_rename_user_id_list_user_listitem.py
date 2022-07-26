# Generated by Django 4.0.6 on 2022-07-18 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='user_id',
            new_name='user',
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('all_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.list')),
            ],
        ),
    ]
