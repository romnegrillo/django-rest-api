from django.shortcuts import render
from django.http import JsonResponse
import json

from products.models import Product

def api_home(request):

    # --------------------------------------------------------------
    # print("Request headers:")
    # print(request.headers)
    # print()

    # print("Request body JSON string:")
    # print(request.body)
    # print(type(request.body))
    # print()

    # print("Request body Python dictionary:")
    # if request.body:
    #     request_body = json.loads(request.body)
    #     print(request_body)
    #     print(type(request_body))
    # else:
    #     print("None")

    # return JsonResponse({"title": "Message from API", "message": "Hello. This message is from API"})
    # --------------------------------------------------------------

    # --------------------------------------------------------------
    product_data = Product.objects.all().order_by("?").first()
    data = {}

    if product_data:
        data["id"] = product_data.id
        data["title"] = product_data.title
        data["content"] = product_data.content
        data["price"] = product_data.price

    return JsonResponse(data)
    # --------------------------------------------------------------