from django.core.management.base import BaseCommand, CommandError
from advocates.models import Advocate, AdvocateRole, Role
import csv
from django.utils import timezone
class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        with open('/Users/samarpitarya/Documents/bar/advocates/management/commands/advocates.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row.get('name').strip().replace("एड", "एडवोकेट") if row.get('name') else None
                phone = row.get('phone') if row.get('phone') else None
                print(f"Name: {name}, Phone: {phone}")
                obj, created = Advocate.objects.get_or_create(
                    name=name,
                    phone=phone,
                )
                # Assign practicing_area with Area IDs 2 and 3
                obj.practice_areas.set([2, 3])
                obj.save()
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Advocate {name} created successfully.'))
        self.stdout.write(self.style.SUCCESS('Advocates imported successfully.'))
