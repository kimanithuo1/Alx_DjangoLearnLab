# bookshelf/management/commands/create_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = "Create default groups and assign permissions"

    def handle(self, *args, **options):
        ct = ContentType.objects.get_for_model(Book)

        perms = {
            'can_view': Permission.objects.get(codename='can_view', content_type=ct),
            'can_create': Permission.objects.get(codename='can_create', content_type=ct),
            'can_edit': Permission.objects.get(codename='can_edit', content_type=ct),
            'can_delete': Permission.objects.get(codename='can_delete', content_type=ct),
        }

        groups = {
            'Viewers': ['can_view'],
            'Editors': ['can_view', 'can_create', 'can_edit'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        for g_name, p_list in groups.items():
            g, created = Group.objects.get_or_create(name=g_name)
            for p in p_list:
                g.permissions.add(perms[p])
            self.stdout.write(self.style.SUCCESS(f'Group {g_name} created/updated with perms: {p_list}'))
