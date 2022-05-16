from django.shortcuts import redirect, render

from inventory.models import Item
from inventory.forms import ItemCreate

# Create your views here.

def create_item_render(request):
    form = ItemCreate()
    print("1 " + request.method)
    
    print("3 " + request.method)
    context = { 'form': form }
    return render(request, 'inventory/create.html', context)

def create_item_post(request):
    if request.method == "POST": # on form submit button click
        print("2 " + request.method)
        form = ItemCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read-inventory')

def read_items(request):
    inventory = Item.objects.all()
    context = {
        'inventory': inventory,
    }
    return render(request, 'inventory/read.html', context)

def update_item(request, **kwargs):
    pk = kwargs.get('yourUUIDFieldName')
    item = Item.objects.get(id=pk)
    form = ItemCreate(instance=item)

    if request.method == "POST": # on update button click
        form = ItemCreate(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('read-inventory')

    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'inventory/update.html', context)

def delete_item(request, **kwargs):
    pk = kwargs.get('yourUUIDFieldName')
    item = Item.objects.get(id=pk)
    
    if request.method == "POST":
        item.delete()
        return redirect('read-inventory')

    context = {"item": item}
    return render(request, 'inventory/delete.html', context)
