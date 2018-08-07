from django.views.generic import View
from django.utils import timezone
from . import models
from pdf_render.render import Render


class Pdf(View):

    def get(self, request):
        sales = models.Sales.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request
        }
        return Render.render('pdf.html', params)