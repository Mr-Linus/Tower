from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from Dashboard import lists
# Create your views here.


class DashboardIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'Dashboard/index.html'

    def get_context_data(self, **kwargs):
        k = lists.K8sList()
        context = super().get_context_data(**kwargs)
        context['k'] = k
        context['task_len'] = len(lists.BreadTask().List_Bread(self.request.user.username))
        context['jobs'] = lists.BreadTask().List_Bread(self.request.user.username)
        return context
