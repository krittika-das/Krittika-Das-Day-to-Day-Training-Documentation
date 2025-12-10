from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def hello(request):
    return JsonResponse({"message": "Django API is working"})

@csrf_exempt
def employees(request):
    if request.method == "GET":
        return JsonResponse({"message": "This is GET"})
    elif request.method == "POST":
        return JsonResponse({"message": "This is POST"})
    elif request.method == "PUT":
        return JsonResponse({"message": "This is PUT"})
    elif request.method == "DELETE":
        return JsonResponse({"message": "This is DELETE"})
    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)
