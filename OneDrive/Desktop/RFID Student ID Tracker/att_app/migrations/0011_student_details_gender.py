
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0010_auto_20180425_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='gender',
            field=models.CharField(blank=True, help_text='Enter Student Gender(M/F/T)', max_length=1, null=True, verbose_name='Student Gender'),
        ),
    ]
