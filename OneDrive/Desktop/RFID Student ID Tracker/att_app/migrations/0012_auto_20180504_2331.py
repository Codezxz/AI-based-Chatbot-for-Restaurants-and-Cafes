

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0011_student_details_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_details',
            name='email',
            field=models.EmailField(blank=True, help_text='Enter Email', max_length=70, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='teacher_details',
            name='gender',
            field=models.CharField(blank=True, help_text='Enter Teacher Gender(M/F/T)', max_length=1, null=True, verbose_name='Teacher Gender'),
        ),
    ]
