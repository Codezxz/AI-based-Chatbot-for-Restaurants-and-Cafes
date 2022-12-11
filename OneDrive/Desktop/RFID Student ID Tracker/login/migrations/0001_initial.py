
from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('sid', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', login.models.MyUserManager()),
            ],
        ),
    ]
