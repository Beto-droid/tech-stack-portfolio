"""
Render Home portfolio
"""
from django.http import HttpResponse

HTML_STING = """
<h1>Hello World</h1>
"""

def home(request):
    """
    Take the request(Django sends a request)
    Return HTML as a response(we pick to return a response)
    """
    response = HttpResponse(HTML_STING, content_type="text/html")
    return response