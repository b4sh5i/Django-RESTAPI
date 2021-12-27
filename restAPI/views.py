from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

from .models import b4sh5i_data
import json
from django.core.serializers import serialize

# Create your views here.
class IndexView(View):
    def get(self, request):
        data = b4sh5i_data.objects.all().order_by('-id')
        ret = json.loads(serialize('json', name))
        return JsonResponse(ret)
    
    def post(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            data = b4sh5i_data(
                idx = request['idx'],
                name = request['name'],
                created_at = request['created_at']
            )
        else:
            data = b4sh5i_data(
                idx = request.POST['idx'],
                name = request.POST['name'],
                created_at = request.POST['created_at']                
            )
        b4sh5i_data.save()
        return HttpResponse(status=200)

    def put(self, request):
        request = json.loads(request.body)
        idx = request['idx']
        name = request['name']
        data = get_object_or_404(b4sh5i_data, pk=idx)
        data.name = name
        data.save()
        return HttpResponse(status=200)

    def delete(self, request):
        request = json.loads(request.body)
        idx = request['idx']
        data = get_object_or_404(b4sh5i_data, pk=idx)
        data.delete()
        return HttpResponse(status=200)