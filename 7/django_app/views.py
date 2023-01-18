from django.shortcuts import render


#
# def index(request):
#     return render(request, 'index.html')


# def contacts(request):
#     return render(request, 'contacts.html')


#
def index(request):
    # generator1 = ({"id": random.randint(0, x), "name": f"Bogdan {x}", "age": x + 20} for x in range(1, 100))

    return render(request, 'todo_app/index.html')
