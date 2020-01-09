import requests as r
import urllib3
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from Image.form import CreatePullForm
# Create your views here.

HoundUrl = "https://192.168.1.102:8080"


class ListView(LoginRequiredMixin, TemplateView):
    urllib3.disable_warnings()
    template_name = 'Image/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nodes'] = json.loads(r.get(HoundUrl+"/nodes/list", verify=False).content.decode())
        context['labels'] = json.loads(r.get(HoundUrl+"/labels/list", verify=False).content.decode())
        return context


class PullView(LoginRequiredMixin, FormView):
    template_name = 'Image/pull.html'
    form_class = CreatePullForm
    success_url = '/image'
    urllib3.disable_warnings()

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        data = {"Label": "all", "imageName": form.cleaned_data['imageName']}
        r.post(HoundUrl+"/labelops/pull", data=data)
        return super().form_valid(form)
