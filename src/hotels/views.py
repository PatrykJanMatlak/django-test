from django.shortcuts import render
from .models import HotelOpinion

# Create your views here.

def hotels_view(request):
    template_name ="hotels/hotel-list.html"
    queryset = HotelOpinion.objects.all()

    context={
        "list2":queryset
    }
    return render(request, template_name, context)