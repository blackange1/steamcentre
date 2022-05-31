from django.shortcuts import render
from .models import Page


def get_page(request, slug):
    page = Page.objects.filter(link=slug)
    if not page:
        return render(request, 'pages/page.html', context={'slug': slug, 'html': '404'})

    context = {
        'html': page[0].html_code,
    }
    return render(request, 'pages/page.html', context=context)
