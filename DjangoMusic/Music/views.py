from django.shortcuts import render, redirect

# import custom modules
from django.core.paginator import Paginator
from . models import Song

# configure how page will work
def index(request):
    paginator = Paginator(Song.objects.all(), 1)    # query songs from data base, display 1
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {"page_obj":page_obj}
    return render(request, "index.html", context)

