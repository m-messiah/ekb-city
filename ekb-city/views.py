# ~*~ coding: utf-8 ~*~

# функция генерирующая 404 страницу
from django.http import Http404, HttpResponse

# функция отрисовки страницы, принимающая путь до шаблона
# и данные помещенные в шаблон
from django.shortcuts import render_to_response
from django.shortcuts import render

import gis

Finder = gis.Finder()


def about(request):
    return render(request, "about.html")


def search(request):
    if 'address' in request.POST and request.POST['address']:
        address = request.POST['address']
        print address.decode("utf-8")
        matches = Finder.match(address)
        return render_to_response('answer.html',
                                  {"address": request.POST['address'],
                                   "matches": sorted(filter(lambda x:
                                                            len(x) > 0,
                                                            matches))
                                   })
    return render(request, "input_form.html")
