from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Restaraunt

# Create your views here.

def all_restaraunts(request):
    """ A view to show all restaraunts, including sorting and search queries """

    restaraunts = Restaraunt.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('restaraunts'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            restaraunts = restaraunts.filter(queries)

    context = {
        'restaraunts': restaraunts,
        'search_term': query,
    }

    return render(request, 'restaraunts/restaraunts.html', context)


def restaraunt_detail(request, restaraunt_id):
    """ A view to show individual restaraunt details """

    restaraunt = get_object_or_404(Restaraunt, pk=restaraunt_id)

    context = {
        'restaraunt': restaraunt,
    }

    return render(request, 'restaraunts/restaraunt_detail.html', context)
