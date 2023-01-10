import os
import sqlite3

import openpyxl
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from todo_app import models


def index(request: HttpRequest) -> HttpResponse:

    data_arr = tuple(({"id": x, "name": f"{x}", "amount": x**2} for x in range(1, 3)))
    print(data_arr, type(data_arr))

    context = {"data_arr": data_arr}

    return render(request, "index.html", context)


