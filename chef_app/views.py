from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChefForm
from .models import Chefs

def home_page(request):
    chefs = Chefs.objects.all()[:3]
    return render(request, 'index.html', {'chefs': chefs})
    # return JsonResponse({"message":"success"})

def contact(request):
    return render(request, 'contact.html')

def chef_list(request):
    chefs = Chefs.objects.all()
    # return render(request, 'chef_list.html', {'chefs': chefs})
    return JsonResponse([str(chef) for chef in chefs], safe=False)

def chef_detail(request, pk):
    chef = get_object_or_404(Chefs, pk=pk)
    return render(request, 'chef_detail.html', {'chef': chef})

def chef_create(request):
    if request.method == 'POST':
        form = ChefForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('chef_list')
    else:
        form = ChefForm()
    return render(request, 'chef_form.html', {'form': form})

def chef_update(request, pk):
    chef = get_object_or_404(Chefs, pk=pk)
    if request.method == 'POST':
        form = ChefForm(request.POST, request.FILES, instance=chef)
        if form.is_valid():
            form.save()
            return redirect('chef_list')
    else:
        form = ChefForm(instance=chef)
    return render(request, 'chef_form.html', {'form': form})

def chef_delete(request, pk):
    chef = get_object_or_404(Chefs, pk=pk)
    if request.method == 'POST':
        chef.delete()
        return redirect('chef_list')
    return render(request, 'chef_confirm_delete.html', {'chef': chef})

def services(request):
    services_data = [
        {
            'title': 'Easy to Order',
            'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero, consectetur!',
            'image': 'Order.jpg',
        },
        {
            'title': 'Fast Delivery',
            'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero, consectetur!',
            'image': 'Fast delivery.jpg',
        },
        {
            'title': 'Best Quality',
            'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero, consectetur!',
            'image': 'Best quality.jpg',
        },
    ]
    return render(request, 'services.html', {'services_data': services_data})
