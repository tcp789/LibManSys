# Generated by Django 2.0.2 on 2018-02-10 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=20)),
                ('library_card_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.User')),
            ],
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.User')),
            ],
            bases=('users.user',),
        ),
        migrations.AddField(
            model_name='user',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='library.Library'),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('patron_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Patron')),
            ],
            bases=('users.patron',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('patron_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Patron')),
            ],
            bases=('users.patron',),
        ),
    ]