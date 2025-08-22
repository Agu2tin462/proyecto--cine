from django.views.generic import TemplateView
from apps.articulo.models import Articulo

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Trae los 3 últimos artículos
        context['articulos'] = Articulo.objects.all().order_by('-fecha_publicacion')[:3]
        return context


class nosotrosView(TemplateView):
    template_name = 'nosotros.html'        
