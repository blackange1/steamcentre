from django.http import HttpResponse
from django.shortcuts import render

from app.forms import StudentForm
from app.models import CardOfMainSlider
from app.my_tools import save_file


def index(request):
    print(CardOfMainSlider.objects.all())
    return render(request,
                  'app/index.html',
                  {
                      'cards': CardOfMainSlider.objects.all()
                  })


def create_cat_main_slider(request):
    if request.method != 'POST':
        student = StudentForm()
        print(dir(student))
        return render(request, "app/create_cat_main_slider.html", {'form': student})
    else:
        cart = CardOfMainSlider.objects.create(
            title=request.POST['title'],
            text=request.POST['text']
        )
        name_img = 'main_slider/item_slider' + str(cart.id)
        type_img = save_file(request.FILES['file'], name_img)
        cart.path_img = 'upload/' + name_img + '.' + type_img
        cart.save()
        return HttpResponse("File uploaded successfuly")
