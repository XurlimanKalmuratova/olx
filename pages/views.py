from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404

from .forms import ClothesForm, ElectronicsForm,  FurnuturesForm, SportsForm, HouseholdsForm

def home(request):
    return render(request, 'base.html')
def about(request):
    return render(request, 'pages/about.html')
def clothes(request):
    clothes = Clothes.objects.all()
    context = {
        'clothes': clothes
        }
    return render(
        request,
        'categories/clothes.html',
        context
    )
def clothes_detail(request, pk):
    try:
        cloth = Clothes.objects.get(id=pk)
    except Clothes.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'cloth': cloth
    }
    return render(
        request,
        'categories/clothes_detail.html',
        context
    )

def electronics(request):
    electronics = Electronics.objects.all()
    context = {
        'electronics': electronics
        }
    return render(request, 'categories/elec.html', context)
def elec_detail(request, pk):
    try:
        electronic = Electronics.objects.get(id=pk)
    except Electronics.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'electronic': electronic
    }
    return render(
        request,
        'categories/elec_detail.html',
        context
    )

def furnitures(request):
    furnitures = Furnutures.objects.all()
    context = {
        'furnitures': furnitures
        }
    return render(request, 'categories/furniture.html', context)
def fur_detail(request, pk):
    try:
        furniture = Furnutures.objects.get(id=pk)
    except Furnutures.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'furniture': furniture
    }
    return render(
        request,
        'categories/fur_detail.html',
        context
    )
def sports(request):
    sports = Sports.objects.all()
    context = {
        'sports': sports
        }
    return render(
        request,
        'categories/sport.html',
        context
    )
def sports_detail(request, pk):
    try:
        sport = Sports.objects.get(id=pk)
    except Sports.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'sport': sport
    }
    return render(
        request,
        'categories/sport_detail.html',
        context
    )
def households(request):
    households = Households.objects.all()
    context = {
        'households': households
        }
    return render(
        request,
        'categories/house.html',
        context
    )
def house_detail(request, pk):
    try:
        household = Households.objects.get(id=pk)
    except Households.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'household': household
    }
    return render(
        request,
        'categories/house_detail.html',
        context
    )
def cart(request):
    return render(request, 'pages/cart.html')


def create(request):
    return render(request, 'pages/create.html')


def createclothes(request):
    if request.method == 'POST':
        form = ClothesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='clothes') 
    else:
        form = ClothesForm()           
    context = {
        'form' : form
    }    
    return render(request, 'creates/createclothes.html', context)

def createelectronics(request):
    if request.method == 'POST':
        form = ElectronicsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='electronics')     
    else:
        form = ElectronicsForm()
    context = {
        'form' : form
    }    
    return render(request, 'creates/createelectronics.html', context)


def createfurniture(request):
    if request.method == 'POST':
        form = FurnuturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='furnitures')     
    else:
        form = FurnuturesForm()        
    context = {
        'form' : form
    }    
    return render(request, 'creates/createfurniture.html', context)

def createsports(request):
    if request.method == 'POST':
        form = SportsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='sports')     
    else:
        form = SportsForm()        
    context = {
        'form' : form
    }    
    return render(request, 'creates/createsports.html', context)


def createhousehold(request):
    if request.method == 'POST':
        form = HouseholdsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='household')     
    else:
        form = HouseholdsForm()        
    context = {
        'form' : form
    }    
    return render(request, 'creates/createhousehold.html', context)


def clothes_delete(request ,pk):
    product = Clothes.objects.get(pk=pk)
    product.delete()
    return redirect(to='clothes')

def electronics_delete(request, pk):
    product = Electronics.objects.get(pk=pk)
    product.delete()    
    return redirect(to='electronics')

def sports_delete(request, pk):
    product = Sports.objects.get(pk=pk)
    product.delete()    
    return redirect(to='sports')

def furniture_delete(request, pk):
    product = Furnutures.objects.get(pk=pk)
    product.delete()    
    return redirect(to='furnitures')

def household_delete(request, pk):
    product = Households.objects.get(pk=pk)
    product.delete()    
    return redirect(to='household')




def clothes_update(request ,pk):
        product = Clothes.objects.get(id=pk)
        form = ClothesForm()
        if request.method == 'POST' :
                form = ClothesForm(request.POST, request.FILES)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    date = form.cleaned_data['date']
                    image = form.cleaned_data['image']
                    description = form.cleaned_data['description']
                    price = form.cleaned_data['price']
                    author = form.cleaned_data['author']
                    author_num = form.cleaned_data['author_num']
                    condition = form.cleaned_data['condition']


                    product.title = title
                    product.date = date
                    product.image = image
                    product.description = description
                    product.price = price
                    product.author = author
                    product.author_num = author_num
                    product.condition = condition
                    product.save()
                    return redirect(to='clothes')
   

        context = {
            'form' : form
        }    

        return render(request, 'update/c.html', context)

def electronics_update(request, pk):
    product = Electronics.objects.get(id=pk)
    form = ClothesForm()
    if request.method == 'POST' :
        form = ElectronicsForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']
            author_num = form.cleaned_data['author_num']
            condition = form.cleaned_data['condition']


            product.title = title
            product.date = date
            product.image = image
            product.description = description
            product.price = price
            product.author = author
            product.author_num = author_num
            product.condition = condition
            product.save()
            return redirect(to='electronics')
    

    context = {
        'form' : form
    }    

    return render(request, 'update/e.html', context)

def sports_update(request, pk):
    product = Sports.objects.get(id=pk)
    form = ClothesForm()
    if request.method == 'POST' :
        form = SportsForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']
            author_num = form.cleaned_data['author_num']
            condition = form.cleaned_data['condition']


            product.title = title
            product.date = date
            product.image = image
            product.description = description
            product.price = price
            product.author = author
            product.author_num = author_num
            product.condition = condition
            product.save()
            return redirect(to='sports')


    context = {
        'form' : form
    }    

    return render(request, 'update/s.html', context)

def furniture_update(request, pk):
    product = Furnutures.objects.get(id=pk)
    form = ClothesForm()
    if request.method == 'POST' :
        form = FurnuturesForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            product.title = cd['title']
            product.date = cd['date']
            product.image = cd['image']
            product.description = cd['description']
            product.price = cd['price']
            product.author = cd['author']
            product.author_num = cd['author_num']
            product.condition = cd['condition']

            product.save()

            return redirect(to='furnitures')
 

    context = {
        'form' : form
    }    

    return render(request, 'update/f.html', context)

def household_update(request, pk):
    product = Households.objects.get(id=pk)
    form = ClothesForm()
    if request.method == 'POST' :
        form = HouseholdsForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']
            author_num = form.cleaned_data['author_num']
            condition = form.cleaned_data['condition']


            product.title = title
            product.date = date
            product.image = image
            product.description = description
            product.price = price
            product.author = author
            product.author_num = author_num
            product.condition = condition
            product.save()

            return redirect(to='household')


    context = {
        'form' : form
    }    
    return render(request, 'update/h.html', context)
