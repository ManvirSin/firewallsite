from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Apply firewall rules'

    def handle(self, *args, **options):
        # Code to communicate with the firewall and apply the rules goes here
        print("Firewall rules applied")
