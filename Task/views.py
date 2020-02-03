from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from Task.k8s import K8sTask
from Task.form import CreateNamespaceForm, CreateJobForm
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


class CreateTaskView(LoginRequiredMixin, FormView):
    template_name = "Task/addjob.html"
    form_class = CreateJobForm
    success_url = "/task"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        cmd = form.cleaned_data['cmd'].split(' ')
        k = K8sTask()
        k.user = self.request.user.username
        k.namespace = form.cleaned_data['namespace']
        k.create_job(
            name=form.cleaned_data['name'],
            image=form.cleaned_data['image'],
            cmd=cmd,
            path="/gf/"+self.request.user,
        )
        return super().form_valid(form)


class DetailTaskView(LoginRequiredMixin, TemplateView):
    template_name = "Task/detail.html"

    def get_context_data(self, **kwargs):
        k = K8sTask()
        k.user = self.request.user.username
        k.namespace = self.kwargs.get('namespace')
        context = super().get_context_data(**kwargs)
        context['result'] = k.log_job(name=self.kwargs.get('name'))
        context['info'] = k.info_job(name=self.kwargs.get('name'))
        context['pod'] = k.get_pod_with_job(self.kwargs.get('name'))
        return context
