import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Item
from .forms import ItemForm


@login_required
def view_items(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'monitor/view_items.html', {'items': items})


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('view_items')
    else:
        form = ItemForm()
    return render(request, 'monitor/add_item.html', {'form': form})


@login_required
def update_item(request, item_id):
    # Fetch the item, ensuring it belongs to the current user
    item = get_object_or_404(Item, id=item_id, user=request.user)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('view_items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'monitor/edit_item.html', {'form': form})


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)  # Ensuring item belongs to the current user
    item.delete()
    return redirect('view_items')


# @login_required
def fetch_current_price(url, selector):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.select_one(selector)
        price = float(price_element.text.strip())
        return price
    except Exception as e:
        print(e)
        return None


@login_required
def check_item_price(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    current_price = fetch_current_price(item.url, item.selector_element)

    if current_price is not None:
        item.current_price = current_price
        item.save()
        messages.success(request, f"Updated the current price for {item.product_name}!")
    else:
        messages.error(request, f"Failed to fetch the price for {item.product_name}. Please try again.")

    return redirect('view_items')
