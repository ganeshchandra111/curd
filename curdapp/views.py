from django.shortcuts import render
from django.http import HttpResponse,Http404

from django.http.response import JsonResponse
from .models import Student
from .serializers import StudentSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentView(APIView):
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Student saved successfully', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get_student(self,pk):
        try:
            student_details = Student.objects.get(studentId=pk)
            return student_details
        except Student.DoesNotExist:
            raise Http404
    
    def get(self,request,pk=None):
        if pk:
            student = self.get_student(pk)
            serializer = StudentSerializers(student)
        else:
            students = Student.objects.all()
            serializer = StudentSerializers(students,many=True)
        
        return Response(serializer.data)


    def put(self, request, pk=None):
        student_to_update = Student.objects.get(studentId=pk)
        serializer = StudentSerializers(instance=student_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse("YESSSSSSSSSSSS",safe=False)
        else:
            return JsonResponse("NOOOOOOOOOOOOOOOOOO",safe=False)

    def delete(self,request,pk):
        student_to_delete = Student.objects.get(studentId=pk)
        student_to_delete.delete()

        return JsonResponse(f"{pk} this guy is deleted",safe=False)
    
def home(requests):
    return HttpResponse('HELOOOOOOOOOOOOOO')
    #this should be seen on the website

