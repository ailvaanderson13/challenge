from django import forms
from django.utils.translation import ugettext_lazy as _

class EditCNPJ(forms.Form):
    TYPE_CHOICES = (
        ('ACTIVE', "Ativo"),
        ('INATIVE', "Inativo")
    )

    active = forms.ChoiceField(
        required=False, label=_('choices'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=TYPE_CHOICES)
    cnpj = forms.CharField(
        label="CNPJ", required=True, widget=forms.TextInput(attrs={'class': 'form-control cnpj-mask', }))
    company_name = forms.CharField(
        label="Nome", required=True, widget=forms.TextInput(attrs={'class': 'form-control', }))

class NewCompany(forms.Form):

    IS_ACTIVE = (
        (True, "Sim"),
        (False, "Não")
    )

    active = forms.ChoiceField(
        required=False, label=_('Ativo'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=IS_ACTIVE)
    cnpj = forms.CharField(
        label="CNPJ", required=True, widget=forms.TextInput(attrs={'class': 'form-control cnpj-mask', }))
    filial_names = forms.CharField(
        label="Nome", required=True, widget=forms.TextInput(attrs={'class': 'form-control', }))

    active_filial = forms.ChoiceField(
        required=False, label="Ativo",
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=IS_ACTIVE)

    company_name = forms.CharField(
        label="Nome", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}))
    

class NewFilial(forms.Form):
    IS_ACTIVE = (
        (True, "Sim"),
        (False, "Não")
    )

    active = forms.ChoiceField(
        required=False, label="Ativo",
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=IS_ACTIVE)

    cnpj = forms.CharField(
        label="CNPJ", required=True, widget=forms.TextInput(attrs={'class': 'form-control cnpj-mask', }))

    company_name = forms.CharField(
        label="Nome", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}))