from django.shortcuts import render
from .models import CountryModel, Poytaxt


def countr_view(request):
    q = request.GET.get('q', '')
    obj = CountryModel.objects.all()
    if q:
        obj = obj.filter(d_name__icontains=q)
    return render(request, 'main/detail.html', context={
        'obj': obj,
        'q': q
    })


def poytaxt_view(request, pk):
    obj1 = Poytaxt.objects.get(id=pk)
    asd = CountryModel.objects.get(id=pk)
    return render(request, 'main/contrib.html', context={
        'obj1': obj1,
        "asd": asd
    })
