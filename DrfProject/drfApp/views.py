'''This views is all about crud using Rest Api'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Teacher
from .serailizer import TeacherSerializer
from .global_msg import MESSAGE

class TestApiView(APIView):
    '''query set or model instance (which are complex data)
      #now converting it into native python datatypes by using serailizer 
      # so that it can rendered into json or xml'''
    def get(self,request):
        '''
        this is for seeing data from database to client
        '''
        modelterm=Teacher.objects.all()
        serailizerterm= TeacherSerializer(modelterm,many=True)
        return Response({MESSAGE:serailizerterm.data},status=status.HTTP_200_OK)
    def post(self,request):
        '''
        This is all about the taking data from client and 
        doing desearializer and ready to store data in database
        '''
        try:
            serailizer=TeacherSerializer(data=request.data)
            if serailizer.is_valid():
                serailizer.save()
                return Response({MESSAGE:"Your data save successfully"},status=status.HTTP_200_OK)
            else:
                return Response({MESSAGE:serailizer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({MESSAGE:"Error :{e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    def put(self,request,id):
        '''This method is for updating the entire data using put'''
        try:
            instance=Teacher.objects.get(id=id)
            serializer=TeacherSerializer(instance=instance,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"Message":"Data update successfully"},status=status.HTTP_200_OK)
            else:
                return Response({MESSAGE:serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({MESSAGE:{e}},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def patch(self,request,id):
        try:
            instance= Teacher.objects.get(id=id)
            serializer=TeacherSerializer(instance=instance,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Messsage":"Data is partially updated"})
            else:
                return Response({MESSAGE:serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({MESSAGE:{e}},status=status.HTTP_502_BAD_GATEWAY)
        
    def delete(self,request,id):
        try:
            instance=Teacher.objects.get(id=id)
            instance.delete()
            return Response({"Message":"Data is deleted"})
        except Teacher.DoesNotExist:
            return Response({MESSAGE:"Data doesnot exists"},status=status.HTTP_404_NOT_FOUND) 
    