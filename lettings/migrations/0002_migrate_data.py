from django.db import migrations

def forwards(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    for old_address in OldAddress.objects.all():
        new_address = NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )

    for old_letting in OldLetting.objects.all():
        new_letting = NewLetting.objects.create(
            title=old_letting.title,
            address=NewAddress.objects.get(id=old_letting.address.id)
        )

def backwards(apps, schema_editor):
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')
    NewAddress.objects.all().delete()
    NewLetting.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
