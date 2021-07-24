from django.conf import settings
from django.shortcuts import get_object_or_404
from restaraunts.models import Restaraunt

def bag_contents(request):

    bag_items = []
    total = 0
    restaraunt_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        restaraunt = get_object_or_404(Restaraunt, pk=item_id)
        total += quantity * restaraunt.price
        restaraunt_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'restaraunt': restaraunt,
        })


    
    grand_total = total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'restaraunt_count': restaraunt_count,
        'grand_total': grand_total,
    }

    return context