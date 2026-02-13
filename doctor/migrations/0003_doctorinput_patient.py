from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('doctor', '0002_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorinput',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diagnoses', to='accounts.patient'),
        ),
    ]
