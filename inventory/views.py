from django.shortcuts import redirect, render

from inventory.models import Item
from inventory.forms import ItemCreate, ItemDelete, ItemRevert

# Create your views here.

deleted = {} # Globally track all deletions


def create_item(request):
    form = ItemCreate()
    
    if request.method == "POST": # on form submit button click
        form = ItemCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read-inventory')

    context = { 'form': form }
    return render(request, 'inventory/create.html', context)

def read_items(request):
    items = Item.objects.all()
    inventory = [i for i in items if i.deleted == False]

    context = {
        'inventory': inventory,
    }
    return render(request, 'inventory/read.html', context)

def update_item(request, **kwargs):
    pk = kwargs.get('yourUUIDFieldName')
    item = Item.objects.get(id=pk)
    print("hello1")

    if request.method == "POST": # on update button click
        form = ItemCreate(request.POST, instance=item)
        print("hello 2")
        if form.is_valid():
            form.save()
            return redirect('read-inventory')

    print("hello3")
    form = ItemCreate(instance=item)        
    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'inventory/update.html', context)

def delete_item(request, **kwargs):
    pk = kwargs.get('yourUUIDFieldName')
    item = Item.objects.get(id=pk)
    form = ItemDelete()
    
    if request.method == "POST":
        form = ItemDelete(request.POST, instance=item)
        if form.is_valid():
            item.deleted=True # bonus requirement 1
            form.save() # Save deletion comment
            return redirect('read-inventory')

    context = {"item": item, "form": form}
    return render(request, 'inventory/delete.html', context)

def deleted_items(request): # bonus requirement 1, deleted comments
    items = Item.objects.all()
    deleted_inventory = [i for i in items if i.deleted]

    context = {
        'deleted_inventory': deleted_inventory,
    }
    return render(request, 'inventory/deleted_items.html', context)


def revert_deleted(request, **kwargs):
    pk = kwargs.get('yourUUIDFieldName')
    item = Item.objects.get(id=pk)
    form = ItemRevert()
    
    if request.method == "POST":
        form = ItemRevert(request.POST, instance=item)
        if form.is_valid():
            item.deleted=False # bonus requirement 1
            item.deleted_comments=""
            form.save() # Save deletion comment
            return redirect('read-inventory')

    context = {"item": item, "form": form}
    return render(request, 'inventory/revert_delete.html', context)
    