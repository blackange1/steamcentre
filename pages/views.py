from django.shortcuts import render
from .models import Page
from django.http import Http404


def get_page(request, slug):
    page = Page.objects.filter(link=slug)
    if not page:
        raise Http404

    context = {
        'html': page[0].html_code,
    }
    return render(request, 'pages/page.html', context=context)
