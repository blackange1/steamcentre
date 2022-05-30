from django.shortcuts import render

from .models import Laboratory, Product


def equipment(request):
    labs = []
    for lab in Laboratory.objects.all().order_by('number_of_lab'):
        products = []
        for product in Product.objects.filter(lab=lab).order_by('number_of_products'):
            products.append(
                {
                    'id': product.number_of_products,
                    'name': product.name,
                    'img': product.img.url,
                    'count': product.count,
                    'for_age': product.for_age,
                    'link_offsite': product.link_offsite,
                    'link_protocol': product.link_protocol,
                    'description': product.description,
                }
            )
        labs.append(
            {
                'id': lab.number_of_lab,
                'name': lab.name,
                'position': lab.img_position.lower(),
                'background_color': lab.background_color,
                'img': lab.img.url,
                'description': lab.description.split('\n'),
                'products': products,
            }
        )

    return render(request, 'equipment/equipment.html', context={'labs': labs})
