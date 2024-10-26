import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

HTML_STR = """
<h1>Hi from inventory management system</h1>"""

def inventory_management_system_home(request):
    number = random.randint(1, 100)

    hrml_sting_to_parse = "HI!"
    asdasd = f"<h1>Hi from inventory management user {number}</h1>"
    response = HttpResponse(asdasd, content_type="text/html")
    return response
