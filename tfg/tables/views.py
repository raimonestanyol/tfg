from django.utils import timezone
from django.views.generic.list import ListView
from .models import Registry

class RegistryListView(ListView):
    model = Registry
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context