from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializers

class StudentView(APIView):
    def get_student(self, pk):
        try:
            return Student.objects.get(studentId=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            student = self.get_student(pk)
            serializer = StudentSerializers(student)
        else:
            students = Student.objects.all()
            serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Student saved successfully', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        student = self.get_student(pk)
        serializer = StudentSerializers(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('Student updated successfully', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_student(pk)
        student.delete()
        return Response(f'Student {pk} deleted successfully', status=status.HTTP_204_NO_CONTENT)
