from django.views.generic import TemplateView
<<<<<<< HEAD

class IndexView(TemplateView):
    template_name = 'index.html'

class peliculaView(TemplateView):
    template_name = 'pelicula.html' 
=======
from apps.articulo.models import Articulo

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Trae los 3 últimos artículos
        context['articulos'] = Articulo.objects.all().order_by('-fecha_publicacion')[:3]
        return context

>>>>>>> 25bdb4c8a5ee3bbd8c2ce3b1657651e1be84f04e

class nosotrosView(TemplateView):
    template_name = 'nosotros.html'        
