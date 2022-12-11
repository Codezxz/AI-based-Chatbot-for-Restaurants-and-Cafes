

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0006_auto_20180215_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='date',
            field=models.CharField(help_text='Enter the Date', max_length=15, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='student_attendance',
            name='in_time',
            field=models.CharField(help_text='Enter the IN Time', max_length=15, null=True, verbose_name='IN Time'),
        ),
        migrations.AlterField(
            model_name='student_attendance',
            name='status',
            field=models.CharField(help_text='Enter the Status', max_length=1, null=True, verbose_name='Student Status'),
        ),
    ]
