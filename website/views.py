from django.shortcuts import render
from datetime import datetime
from .models import Avocado_Price
from .models import City_House_Price
from .utils import get_plot

def avocado_data(request):
	price_list = Avocado_Price.objects.all()
	return render(request, 'website/avocado_price_data.html', {"price_list" : price_list})

def home_data(request):
	price_list = City_House_Price.objects.all()
	x = [x.city for x in price_list]
	y = [y.average_price for y in price_list]
	chart = get_plot(x,y)
	return render(request, 'website/house_price_data.html', {"price_list" : price_list, "chart" : chart })



# Create your views here.
def home(request):
	name ="Allison"
	now = datetime.now()
	current_year = now.year
	price_list = Avocado_Price.objects.all()
	return render(request, 'website/home.html',{"name" : name, "current_year" : current_year, "price_list" : price_list})