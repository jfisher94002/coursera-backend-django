# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {
        "menu": menu_data
    }
    return render(request, 'menu.html', main_data)

def display_menu_item(request, pk=None):
    if pk:
    # Create a variable menu_item and assign it the value of objects.get(pk=pk) 
    # which is called over the Menu model class .
        menu_item = Menu.objects.get(pk=pk)

    # else:
    else:
    # Assign an empty string to the variable menu_item
        menu_item = ''
    return render(request, 'menu_item.html', {'menu_item': menu_item})

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views