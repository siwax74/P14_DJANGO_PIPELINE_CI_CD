from django.db import migrations

def migrate_address_and_letting(apps, schema_editor):
    OldAddress = apps.get_model('lettings', 'Address')
    OldLetting = apps.get_model('lettings', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    old_to_new_address_map = {}

    # Copier les adresses
    for addr in OldAddress.objects.all():
        new_addr = NewAddress.objects.create(
            number=addr.number,
            street=addr.street,
            city=addr.city,
            state=addr.state,
            zip_code=addr.zip_code,
            country_iso_code=addr.country_iso_code,
        )
        old_to_new_address_map[addr.id] = new_addr

    # Copier les lettings
    for let in OldLetting.objects.all():
        NewLetting.objects.create(
            title=let.title,
            address=old_to_new_address_map[let.address_id]
        )

class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_address_and_letting),
    ]
