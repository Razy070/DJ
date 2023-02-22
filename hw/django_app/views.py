from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Hello world")


# def index(request: HttpRequest) -> HttpResponse:
#
#     data_arr = tuple(({"id": x, "name": f"{x}", "amount": x**2} for x in range(1, 3)))
#     print(data_arr, type(data_arr))
#
#     context = {"data_arr": data_arr}
#
#     return render(request, "index.html", context)
