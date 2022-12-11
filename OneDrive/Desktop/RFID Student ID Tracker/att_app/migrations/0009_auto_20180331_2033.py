
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0008_student_details_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='email',
            field=models.EmailField(blank=True, help_text='Enter Email', max_length=70, null=True, unique=True, verbose_name='Email'),
        ),
    ]
