import requests as r
import urllib3
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
# Create your views here.

HoundUrl = "https://192.168.1.102:8080"


class NodeListView(LoginRequiredMixin, TemplateView):
    urllib3.disable_warnings()
    nodes = json.loads(r.get(HoundUrl+"/nodes/list", verify=False).content.decode())

