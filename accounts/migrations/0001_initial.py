# Generated by Django 2.0.8 on 2019-04-06 06:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_company', models.BooleanField(default=False)),
                ('is_recruiter', models.BooleanField(default=False)),
                ('is_freelancer', models.BooleanField(default=False)),
                ('is_candidate', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CTC_from', models.CharField(default='1000000', max_length=100)),
                ('CTC_to', models.CharField(default='100000', max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('job_type', models.CharField(default='internship', max_length=100)),
                ('Location', models.CharField(default='Ranchi', max_length=1000)),
                ('Qualification', models.CharField(default='BE', max_length=1000)),
                ('job_decription', models.TextField()),
                ('min_exp', models.CharField(default='less than one year', max_length=1000)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=12)),
                ('ug_college', models.CharField(max_length=70)),
                ('ug_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pg_college', models.CharField(blank=True, max_length=70)),
                ('pg_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('work_exp', models.DecimalField(decimal_places=0, max_digits=2)),
                ('resume', models.FileField(upload_to='users/resumes')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('website', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('Qualification', models.CharField(max_length=1000)),
                ('Location', models.CharField(max_length=1000)),
                ('PAN', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('Company_name', models.CharField(max_length=100)),
                ('PAN', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]