from multiprocessing import context
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from ..clientes.models import Clients, Filial
from django.views.generic.edit import UpdateView, FormView, CreateView
from django.db.models import Q
from .forms import NewCompany, NewFilial
from django.http import JsonResponse


class ListClients(FormView):
    template_name = "clients.html"
    form_class = NewCompany

    
    def get_initial(self):
        initial = dict()

        for item in ['cnpj', 'filial_names', 'company_name', 'active_filial',
                     'active']:
            initial[item] = None

        if self.request.GET.get('sample', False):
            model = Clients.objects.get(id=self.request.GET['sample'])
            initial['cnpj'] = model.bedroom
            initial['filial_names'] = model.suite
            initial['company_name'] = model.bathroom
            initial['active_filial'] = model.total_area
            initial['active'] = model.total_area

        print(initial)
        return initial

class AddClient(View):
    def  get(self, request):
        company_name1 = request.GET.get('company_name', None)
        active1 = request.GET.get('active', None)

        obj = Clients.objects.create(
            active = active1,
            company_name = company_name1,
        )
        
        context = Clients.objects.values()
        context.append({'id':obj.id,'active':obj.active,'company':obj.company})

        data = {
            'context': context
        }
        return JsonResponse(data)


class AddFilial(View):

    def  get(self, request):
        active1 = request.GET.get('name', None)
        filialname1 = request.GET.get('address', None)
        cnpj1 = request.GET.get('age', None)

        obj = Filial.objects.create(
            active = active1,
            filial_name = filialname1,
            cnpj = cnpj1
        )
        
        context = Filial.objects.filter(company=self.request.company_pk).values()
        context.append({'id':obj.id,'active':obj.active,'filial_name':obj.filial_name,'cnpj':obj.cnpj})

        data = {
            'context': context
        }
        return JsonResponse(data)

