from django.shortcuts import render
from .models import Restaraunt

# Create your views here.


def all_restaraunts(request):
    """A view to show all restaraunts, including sorting and search queries """

    restaraunts = Restaraunt.objects.all()

    context = {
        'restaraunts': restaraunts,
    }

    return render(request, 'restaraunts/restaraunts.html', context)
