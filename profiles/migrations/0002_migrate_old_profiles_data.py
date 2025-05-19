from django.db import migrations

def migrate_profiles(apps, schema_editor):
    OldProfile = apps.get_model('profiles', 'Profile')
    User = apps.get_model('auth', 'User')
    NewProfile = apps.get_model('profiles', 'Profile')

    for old in OldProfile.objects.all():
        NewProfile.objects.create(
            user=User.objects.get(id=old.user_id),
            favorite_city=old.favorite_city,
        )


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_profiles),
    ]
