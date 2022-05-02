from django.http import HttpResponse
from django.shortcuts import render

from app.models import MainSlider
from app.my_tools import save_file


def index(request):
    print(MainSlider.objects.all())
    return render(request,
                  'app/index.html',
                  {
                      'cards': MainSlider.objects.all()
                  })
