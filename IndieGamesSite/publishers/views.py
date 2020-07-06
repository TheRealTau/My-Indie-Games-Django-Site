from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Publisher


# Create your views here.
class PubListView(ListView):
    model = Publisher
    template_name = 'publishers/publishers_list.html'
    paginate_by = 4  
    context_object_name = 'publishers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publisher'] = Publisher.objects.all()

        return context

class PubDetailView(DetailView):
    model = Publisher
    template_name = 'publishers/publisher_detail.html'

    def get_object(self):
        return get_object_or_404(Publisher, pk=self.kwargs['pk'])
