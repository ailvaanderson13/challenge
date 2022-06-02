from multiprocessing import context
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from ..clientes.models import Clients
from django.views.generic.list import ListView
from ..clientes.forms import NewCompany

class Home(ListView):
    template_name = "home.html"
    model = Clients
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context['companys'] = self.model.objects.all().count()

        return context  