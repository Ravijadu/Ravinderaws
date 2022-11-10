from django.shortcuts import render,redirect
from .forms import spalfeedback


# Create your views here.
def feedback(request):
  if request.method == 'POST':
    fm = spalfeedback(request.POST,request.FILES)
    if fm.is_valid():
      fm.save()
      fm = spalfeedback()
      return redirect('index')
  else:
    fm = spalfeedback()
  return render(request,'Feedback/feedback.html',{'form':fm})




