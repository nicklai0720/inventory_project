from django.shortcuts import render, get_object_or_404, redirect
from .models import Factory, Product, Material, Item
from django.utils import timezone
from .forms import ItemForm, ItemForm_private

def home(request):
    return render(request, 'home.html')

# def public_items(request):
#     items = Item.objects.filter(factory__name='公版')
#     return render(request, 'public_items.html', {'items': items})

def private_items(request):
    items = Item.objects.exclude(factory__name='公版')
    form = ItemForm_private()

    if request.method == 'POST':
        form = ItemForm_private(request.POST)
        if form.is_valid():
            form.save()  # 如果表單有效，保存到數據庫
            return redirect('private_items')  # 重定向到公共項目頁面

    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'private_items.html', context)

def update_stock(request, item_id):
    if request.method == 'POST':
        new_stock = request.POST.get('new_stock')
        item = get_object_or_404(Item, id=item_id)
        item.current_stock = new_stock
        item.last_updated = timezone.now()
        item.save()
    return redirect('public_items')

def update_private_stock(request, item_id):
    if request.method == 'POST':
        new_stock = request.POST.get('new_stock')
        item = get_object_or_404(Item, id=item_id)
        item.current_stock = new_stock
        item.last_updated = timezone.now()
        item.save()
    return redirect('private_items')

def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        item.delete()
    return redirect('public_items')

def delete_private_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        item.delete()
    return redirect('private_items')

# def manage_stock(request):
#     if request.method == 'POST':
#         item_id = request.POST.get('item_id')
#         new_stock = request.POST.get('new_stock')
#         item = get_object_or_404(Item, id=item_id)
#         item.current_stock = new_stock
#         item.last_updated = timezone.now()
#         item.save()
#         return redirect('manage_stock')
#     items = Item.objects.all()
#     return render(request, 'manage_stock.html', {'items': items})

def public_chart(request):
    data = {}
    items = Item.objects.filter(factory__name='公版')
    for item in items:
        data[item.__str__()] = [item.current_stock]
    return render(request, 'public_chart.html', {'data': data})

# def private_chart(request):
#     data = {}
#     items = Item.objects.exclude(factory__name='公版')
#     for item in items:
#         data[item.__str__()] = [item.current_stock]
#     return render(request, 'private_chart.html', {'data': data})

def private_chart(request):
    data = {}
    items = Item.objects.exclude(factory__name='公版')
    for item in items:
        factory_name = item.factory.name
        if factory_name not in data:
            data[factory_name] = [0]
        data[factory_name][0] += item.current_stock
    return render(request, 'private_chart.html', {'data': data})

def factory_chart(request, factory_name):
    items = Item.objects.filter(factory__name=factory_name)
    data = {item.__str__(): item.current_stock for item in items}
    return render(request, 'factory_chart.html', {'factory_name': factory_name, 'data': data})

def public_items(request):
    items = Item.objects.filter(factory__name='公版')  # 獲取所有項目
    form = ItemForm()  # 創建一個空的 ItemForm

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()  # 如果表單有效，保存到數據庫
            return redirect('public_items')  # 重定向到公共項目頁面

    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'public_items.html', context)

def backend(request):
    factories = Factory.objects.all()
    products = Product.objects.all()
    materials = Material.objects.all()
    return render(request, 'backend.html', {'factories': factories, 'products': products, 'materials': materials})
