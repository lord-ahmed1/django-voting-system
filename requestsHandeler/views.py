from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from validate_docbr import CPF
import json
@csrf_exempt
def checkCPF(request):
    json_data=json.loads(request.body)
    cpf=CPF()
    validate=cpf.validate(json_data["cpf"])
    return HttpResponse(validate)


# Create your views here.
