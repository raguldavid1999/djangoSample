from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def home(request):
    context = {}
    return render(request, 'myAppTemp/index.html',context)

class sampleAPI(APIView):
    def get(self, request):
        return Response([
            {
                'name': 'Abhishek',
                'age': 20
            }
        ])