from django.shortcuts import render,redirect
from .forms import OwnerRegistration
from django.contrib.auth.decorators import login_required
from .forms import OwnerDetail
from realtors.models import Realtor

# Create your views here.
@login_required(login_url='login')
def owner(request):
  if request.method == 'POST':
    fm = OwnerRegistration(request.POST,request.FILES)
    if fm.is_valid():
      fm.save()
      fm = OwnerRegistration()
      return redirect('index')
  else:
    fm = OwnerRegistration()
  return render(request,'OwnerListing/owner.html',{'form':fm})

@login_required(login_url='login')
def ownerdetail(request):
  if request.method == 'POST':
    fm = OwnerDetail(request.POST,request.FILES)
    if fm.is_valid():
      fm.save()
      name = request.POST['name']
      fm = OwnerDetail()
      return redirect('owner')
  else:
    fm = OwnerDetail()
  return render(request,'OwnerListing/ownerdetail.html',{'form':fm})



