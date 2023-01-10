from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect


# from todo_app import models as django_models


def index(request):
    # generator1 = ({"id": random.randint(0, x), "name": f"Bogdan {x}", "age": x + 20} for x in range(1, 100))

    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, 'todo_app/index.html', context=data)
# # Create your views here.
#
#
# def home(request):
#     return render(request, 'todo_app/index.html')
#
#
# def my_api_one(request: HttpRequest, post_id: int) -> JsonResponse:
#     datas = [
#         {
#             "userId": int(round(post_id / 10, 0)),
#             "id": post_id,
#         }
#     ]
#
#     return JsonResponse(data=datas, safe=False)
#
#
# def my_api(request):
#     datas = [
#         {
#             "userId": round(x / 10, 0),
#             "id": x,
#         }
#         for x in range(1, 100 + 1)
#     ]
#     return JsonResponse(data=datas, safe=False)
