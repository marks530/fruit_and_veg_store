from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    weight = None
    if product_weight in request.POST:
        weight = request.POST['product_weight']
    bag = request.session.get('bag', {})

    if weight:
        if item_id in list(bag.keys()):
            if weight in bag[item_id]['items_by_weight'].keys():
                bag[item_id]['items_by_weight'][weight] += quantity
            else:
                bag[item_id]['items_by_weight'][weight] = quantity
        else:
            bag[item_id] = {'items_by_weight': {weight: quantity}}
    else:
        bag[item_id] = quantity
        
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)