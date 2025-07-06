from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
import random
from faker import Faker

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        self.create_users()
        self.create_listings()
        self.stdout.write(self.style.SUCCESS('Successfully seeded data!'))

    def create_users(self):
        # Create a test host if not exists
        if not User.objects.filter(email='host@example.com').exists():
            User.objects.create_user(
                username='host',
                email='host@example.com',
                password='testpass123',
                is_active=True
            )

        # Create a test guest if not exists
        if not User.objects.filter(email='guest@example.com').exists():
            User.objects.create_user(
                username='guest',
                email='guest@example.com',
                password='testpass123',
                is_active=True
            )

    def create_listings(self):
        property_types = ['apartment', 'house', 'villa', 'cabin']
        host = User.objects.get(email='host@example.com')

        for i in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                address=fake.address(),
                city=fake.city(),
                country=fake.country(),
                price_per_night=random.randint(50, 500),
                property_type=random.choice(property_types),
                num_bedrooms=random.randint(1, 5),
                num_bathrooms=random.randint(1, 3),
                max_guests=random.randint(1, 10),
                amenities=', '.join(fake.words(nb=5)),
                host=host
            )