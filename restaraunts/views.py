from django.shortcuts import render, get_object_or_404
from .models import Restaraunt

# Create your views here.


def all_restaraunts(request):
    """ A view to show all restaraunts, including sorting and search queries """

    restaraunts = Restaraunt.objects.all()

    context = {
        'restaraunts': restaraunts,
    }

    return render(request, 'restaraunts/restaraunts.html', context)


def restaraunt_detail(request, restaraunt_id):
    """ A view to show individual restaraunt details """

    restaraunt = get_object_or_404(Restaraunt, pk=restaraunt_id)

    context = {
        'restaraunt': restaraunt,
    }

    return render(request, 'restaraunts/restaraunt_detail.html', context)