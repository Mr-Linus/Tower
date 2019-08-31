from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from Dashboard import lists
# Create your views here.


class DashboardIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'Dashboard/index.html'

    def get_context_data(self, **kwargs):
        k = lists.K8S()
        context = super().get_context_data(**kwargs)
        context['node_num'] = k.node_num()
        context['pod_num'] = k.pod_num()
        context['namespace_num'] = k.namespace_num()
        context['job_num'] = k.job_num()
        return context
