from django.shortcuts import render
from django.views.generic import TemplateView
from . import barmicva

class HomePageView(TemplateView):
    template_name="hebcount/home.html"

def kalkul(request):
    error_msg=None
    datum=None
    shabbat=None
    parasha=None
    sex=request.POST.get('sex')
    sex=True if sex else False
    sunset=request.POST.get('sunset')
    sunset=True if sunset else False
    if request.method=="POST":
        count=barmicva.Bmicva(request.POST["year"], request.POST["month"], request.POST["day"], sex, sunset)
        count.to_hebcal()
        count.bmicva_date()
        datum=count.printing()
        shabbat=count.bmicva()
        parasha=count.parasha()
    return render(request, 'hebcount/bmicva.html', dict(error_msg=error_msg, datum=datum, shabbat=shabbat, parasha=parasha))

            



# Create your views here.
