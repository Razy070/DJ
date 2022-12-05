from django.shortcuts import render, redirect


# from django_app import models as django_models


def index(request):
    # generator1 = ({"id": random.randint(0, x), "name": f"Bogdan {x}", "age": x + 20} for x in range(1, 100))

    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, 'django_app/home.html', context=data)

