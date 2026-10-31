from .models import CarMake, CarModel

CARS = {
    "Nissan": ("Japan", [("Pathfinder", "SUV"), ("Qashqai", "SUV"), ("XTRAIL", "SUV")]),
    "Mercedes": ("Germany", [("A-Class", "SEDAN"), ("C-Class", "SEDAN"), ("E-Class", "SEDAN")]),
    "Audi": ("Germany", [("A4", "SEDAN"), ("A5", "COUPE"), ("A6", "SEDAN")]),
    "Kia": ("South Korea", [("Sorrento", "SUV"), ("Carnival", "SUV"), ("Cerato", "SEDAN")]),
    "Toyota": ("Japan", [("Camry", "SEDAN"), ("Corolla", "SEDAN"), ("Highlander", "SUV")]),
}


def initiate():
    for make_name, (country, models_) in CARS.items():
        make, _ = CarMake.objects.get_or_create(
            name=make_name,
            defaults={"description": f"Great cars. {make_name}", "country": country})
        for name, type_ in models_:
            CarModel.objects.get_or_create(
                car_make=make, name=name, defaults={"type": type_, "year": 2023})
