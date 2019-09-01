from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
# Create your views here.


class NamespaceView(LoginRequiredMixin, TemplateView):
    template_name = 'Task/namespace.html'



