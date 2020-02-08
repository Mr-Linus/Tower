from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from Service.form import CreateServiceForm
from django.shortcuts import redirect
from Service.Service import Service

StartPort = 11000


# Create your views here.
class ServiceView(LoginRequiredMixin, FormView):
    template_name = 'Service/service.html'
    success_url = '/service/'
    form_class = CreateServiceForm

    def form_valid(self, form):
        global StartPort
        StartPort += 1
        Service().Create_Service(name=form.cleaned_data['name'],
                                 namespace=self.request.user.username,
                                 port=StartPort
                                 )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service().List_Service(self.request.user.username)
        context['number'] = Service().Number_Service(self.request.user.username)
        return context


class DeleteServiceView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        Service().Delete_Service(name=self.kwargs.get('name'),
                                 namespace=self.request.user.username)
        return redirect("/service")
