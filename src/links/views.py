from django.shortcuts import render, redirect
from .forms import AddLinkForm
from .models import Link
# Create your views here.
def home_view(request):
	no_discounted = 0
	error = None
	form = AddLinkForm(request.POST or None)
	if request.method=="POST":
		try:
			if form.is_valid():
				form.save()
		except AttributeError:
			error = "Oops... Couldn't get the name or the price"
		except:
			error = "Oops... Something went wrong"
	form = AddLinkForm()
	qs = Link.objects.all()
	items_no = qs.count()

	if items_no>0:
		discount_list=[]
		for item in qs:
			if item.old_price< item.current_price:
				discount_list.append(item)
		no_discounted = len(discount_list)

	context={
	'qs':qs,
	'items_no':items_no,
	'no_discounted': no_discounted,
	'form':form,
	'error':error
	}

	return render(request,"./links/index.html",context)

def update_view(request):
	qs = Link.objects.all()
	for items in qs:
		items.save()
	return redirect('home')

def delete_view(request,pk):
	item = Link.objects.filter(pk=pk)
	item.delete()
	return redirect('home')