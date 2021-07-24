from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Restaraunt, Category
from django.db.models.functions import Lower

# Create your views here.

def all_restaraunts(request):
    """ A view to show all restaraunts, including sorting and search queries """

    restaraunts = Restaraunt.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                restaraunts = restaraunts.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            restaraunts = restaraunts.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            restaraunts = restaraunts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('restaraunts'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            restaraunts = restaraunts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'restaraunts': restaraunts,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'restaraunts/restaraunts.html', context)


def restaraunt_detail(request, restaraunt_id):
    """ A view to show individual restaraunt details """

    restaraunt = get_object_or_404(Restaraunt, pk=restaraunt_id)

    context = {
        'restaraunt': restaraunt,
    }

    return render(request, 'restaraunts/restaraunt_detail.html', context)