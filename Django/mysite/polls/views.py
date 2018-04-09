from django.http import HttpResponse

# Create your views here.
def index(request):
    response: HttpResponse = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is polls app")
    return  response