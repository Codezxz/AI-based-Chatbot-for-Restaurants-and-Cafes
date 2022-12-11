

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0009_auto_20180331_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='in_time',
            field=models.CharField(blank=True, help_text='Enter the IN Time', max_length=15, null=True, verbose_name='IN Time'),
        ),
    ]
