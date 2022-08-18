from django.views.generic import ListView
from .models import Episode


class HomePageView(ListView):
    model = Episode
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['episodes'] = Episode.objects.filter().order_by('-pub_date')[:10]
        return context