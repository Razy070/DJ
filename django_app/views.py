from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest


# Create your views here.


def home(request):
    return render(request, 'django_app/home.html')


def my_api_one(request: HttpRequest, post_id: int) -> JsonResponse:
    datas = [
        {
            "userId": int(round(post_id / 10, 0)),
            "id": post_id,
        }
    ]

    return JsonResponse(data=datas, safe=False)


def my_api(request):
    datas = [
        {
            "userId": round(x / 10, 0),
            "id": x,
        }
        for x in range(1, 100 + 1)
    ]
    return JsonResponse(data=datas, safe=False)
