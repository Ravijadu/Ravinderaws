from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices,district_choices,state_choices
from django.contrib.auth.decorators import login_required


from .models import Listing


def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)


@login_required(login_url='login')
def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # title
  if 'title' in request.GET:
    title = request.GET['title']
    if title:
      queryset_list = queryset_list.filter(title__icontains=title) | queryset_list.filter(state__icontains=title) | queryset_list.filter(district__icontains=title)



  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state=state)

  # district
  if 'district' in request.GET:
    district= request.GET['district']
    if district:
      queryset_list = queryset_list.filter(district=district)


  context = {
    'state_choices' : state_choices,
    'district_choices': district_choices,
    'listings': queryset_list,
    'values': request.GET,
  }

  return render(request, 'listings/search.html', context)
