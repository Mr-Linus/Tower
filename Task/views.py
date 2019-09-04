from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from Task.k8s import K8sTask
from Task.form import CreateNamespaceForm
import time
# Create your views here.


class NamespaceView(LoginRequiredMixin, FormView):
    template_name = 'Task/namespace.html'
    form_class = CreateNamespaceForm
    success_url = '/task/namespace/'

    def get_context_data(self, **kwargs):
        k = K8sTask()
        k.user = self.request.user.username
        context = super().get_context_data(**kwargs)
        context['k'] = k
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        k = K8sTask()
        k.user = self.request.user.username
        k.namespace = form.cleaned_data['namespace']
        k.create_namespace()
        return super().form_valid(form)


class DeleteNamespaceView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        k = K8sTask()
        k.namespace = self.kwargs.get('name')
        k.delete_namespace()
        return redirect("/task/namespace")


class TaskView(LoginRequiredMixin, TemplateView):
    template_name = 'Task/task.html'

    def get_context_data(self, **kwargs):
        k = K8sTask()
        k.user = self.request.user.username
        context = super().get_context_data(**kwargs)
        context['k'] = k
        return context


class DeleteTaskView(LoginRequiredMixin, TemplateView):
    template_name = "Task/task.html"

    def get(self, request, *args, **kwargs):
        k = K8sTask()
        k.user = self.request.user.username
        k.namespace = self.kwargs.get('namespace')
        k.delete_job(self.kwargs.get('name'))
        time.sleep(1)
        return redirect("/task")
