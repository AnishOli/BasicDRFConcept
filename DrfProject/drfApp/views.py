from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Teacher
from .serailizer import TeacherSerializer


class TestApiView(APIView):
    def get(self,request):
        modelterm=Teacher.objects.all() # query set or model instance (which are complex data)
        #now converting it into native python datatypes by using serailizer so that it can rendered into json or xml
        serailizerterm= TeacherSerializer(modelterm,many=True)    
        return Response({"message":serailizerterm.data})
        
