from django.shortcuts import render
from .models import Stock
# from .filters import StockFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'stock-watcher/home.html', {'title': 'Home'})


def stock_search(request):
    f = EmptyPage(request.GET, queryset=Stock.objects.all())
    paginator = Paginator(f.qs)

    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    return render(request, 'stock-watcher/search_results.html', {'filter': response, 'filter_form': f})
