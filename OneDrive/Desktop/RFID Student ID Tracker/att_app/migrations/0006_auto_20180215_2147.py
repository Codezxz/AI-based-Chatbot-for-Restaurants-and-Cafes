

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0005_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='s_class',
            field=models.CharField(help_text='Enter Student Class', max_length=1, null=True, verbose_name='Student Class'),
        ),
        migrations.AddField(
            model_name='student_details',
            name='sec',
            field=models.CharField(help_text='Enter Student Section', max_length=1, null=True, verbose_name='Student Section'),
        ),
    ]
