from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from Task.k8s import K8sTask, BreadTask
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
        context['len'] = len(k.get_user_namespace())
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # TODO: The Namespace function will be remove
        k = K8sTask()
        k.user = self.request.user.username
        k.namespace = self.request.user.username
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
        context = super().get_context_data(**kwargs)
        context['tasks'] = BreadTask().List_Bread(self.request.user.username)
        context['len'] = len(context['tasks'])
        return context


class DeleteTaskView(LoginRequiredMixin, TemplateView):
    template_name = "Task/task.html"

    def get(self, request, *args, **kwargs):
        BreadTask().Delete_Bread(
            namespace=self.kwargs.get('namespace'),
            name=self.kwargs.get('name'))
        time.sleep(1)
        return redirect("/task")


class CreateTaskView(LoginRequiredMixin, FormView):
    template_name = "Task/addtask.html"
    form_class = CreateJobForm
    success_url = "/task"

    def form_valid(self, form):
        framework = form.cleaned_data['framework'].split('-')[0]
        version = form.cleaned_data['framework'].split('-')[1]
        BreadTask().Creat_Bread(
            name=form.cleaned_data['name'],
            namespace=self.request.user.username,
            gpu=form.cleaned_data['gpu'],
            mem=form.cleaned_data['memory'],
            level=form.cleaned_data['level'],
            command=form.cleaned_data['cmd'],
            framework=framework,
            version=version,
            task_type=form.cleaned_data['type'],
            path=self.request.user.username
        )
        return super().form_valid(form)


# TODO: Need to Fix
class DetailTaskView(LoginRequiredMixin, TemplateView):
    template_name = "Task/detail.html"

    def get_context_data(self, **kwargs):
        b = BreadTask()
        context = super().get_context_data(**kwargs)
        context['pod'] = b.Get_Pod_Info(name=self.kwargs.get('name'),
                                        namespace=self.request.user.username)
        context['result'] = b.Get_Pod_Logs(name=self.kwargs.get('name'),
                                           namespace=self.request.user.username)
        return context

