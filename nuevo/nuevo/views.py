from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class peliculaView(TemplateView):
    template_name = 'pelicula.html' 

class nosotrosView(TemplateView):
    template_name = 'nosotros.html'        
