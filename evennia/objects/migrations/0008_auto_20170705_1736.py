# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 17:36
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):

    try:
        apps.get_model('players', 'PlayerDB')
    except LookupError:
        return
    AccountDB = apps.get_model('accounts', 'AccountDB')
    ObjectDB = apps.get_model('objects', 'ObjectDB')

    for object in ObjectDB.objects.all():
        player = object.db_player
        if player:
            account = AccountDB.objects.get(id=player.id)
            object.db_account = account
            object.save(update_fields=['db_account'])

class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0007_objectdb_db_account'),
    ]

    operations = [
        migrations.RunPython(forwards)
    ]