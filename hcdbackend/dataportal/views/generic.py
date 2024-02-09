from django.shortcuts import render

from dataportal.models import Species, Area, Animal, AnimalReport

MODEL_LU = {"/dataportal/area": {"model": Area, "title": "area"},
            "/dataportal/animal": {"model": Animal, "title": "animal"},
            "/dataportal/species": {"model": Species, "title": "species"}
            }


def generic_all(request):
    generic_model = MODEL_LU[request.path_info]
    generic_objects = generic_model['model'].objects.all()
    context = {"generic_objects": generic_objects,
               "title": generic_model['title']}
    return render(request, "dataportal/generic_all.html", context)


def generic_detail(request, pk):
    generic_model = MODEL_LU[request.path_info.rsplit("/", 1)[0]]
    generic_object = generic_model['model'].objects.get(pk=pk)
    context = {"generic_object": generic_object,
               "title": generic_model['title']}

    return render(request, "dataportal/generic_detail.html", context)
