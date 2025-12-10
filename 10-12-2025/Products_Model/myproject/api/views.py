from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json

def hello(request):
    return JsonResponse({"message": "Hello World!"})

@csrf_exempt
def products(request):

    # GET ALL EMPLOYEES
    if request.method == "GET":
        data = list(Product.objects.values())
        return JsonResponse(data, safe=False)

    # CREATE EMPLOYEE
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Product.objects.create(
            name=body["name"],
            typ=body["typ"],
            price=body["price"],
            warranty=body["warranty"]
        )
        return JsonResponse({"message": "POST EXECUTED"})

    # UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        emp = Product.objects.get(id=body["id"])
        emp.name = body["name"]
        emp.typ = body["typ"]
        emp.price = body["price"]
        emp.warranty = body["warranty"]
        emp.save()
        return JsonResponse({"message": "PUT EXECUTED"})

    # DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        emp = Product.objects.get(id=body["id"])
        emp.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
