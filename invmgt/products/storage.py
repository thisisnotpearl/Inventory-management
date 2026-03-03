from django.utils import timezone
from decimal import Decimal

data = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "EL",
        "quantity": 10,
        "price": Decimal("55000.00"),
        "brand": "Dell",
        "date_added": timezone.now()
    },
    {
        "id": 2,
        "name": "Wireless Mouse",
        "category": "EL",
        "quantity": 45,
        "price": Decimal("799.00"),
        "brand": "Logitech",
        "date_added": timezone.now()
    },
    {
        "id": 3,
        "name": "Office Chair",
        "category": "FR",
        "quantity": 8,
        "price": Decimal("7200.00"),
        "brand": "GreenSoul",
        "date_added": timezone.now()
    },
    {
        "id": 4,
        "name": "Notebook Pack",
        "category": "ST",
        "quantity": 120,
        "price": Decimal("250.00"),
        "brand": "Classmate",
        "date_added": timezone.now()
    },
    {
        "id": 5,
        "name": "Water Bottle",
        "category": "AC",
        "quantity": 60,
        "price": Decimal("399.00"),
        "brand": "Milton",
        "date_added": timezone.now()
    }
]

id_counter = 6