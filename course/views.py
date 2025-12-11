from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer


# only admin allowed
def is_admin(user):
    # safe check: avoids crash if role not present
    return user.is_authenticated and getattr(user, "role", None) == "ADMIN"


class CourseList(APIView):
    ####
    #GET  /course/courselist/        -> list all courses
    #POST /course/courselist/        -> create course (ADMIN only)
    ####

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not is_admin(request.user):
            return Response(
                {'msg': "Only admin can add the course"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            return Response(
                CourseSerializer(course).data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    """
    GET    /course/coursedetail/<id>/   -> get single course
    PUT    /course/coursedetail/<id>/   -> full update (ADMIN only)
    PATCH  /course/coursedetail/<id>/   -> partial update (ADMIN only)
    DELETE /course/coursedetail/<id>/   -> delete (ADMIN only)
    """

    def get_object(self, pk):
        return get_object_or_404(Course, pk=pk)

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        if not is_admin(request.user):
            return Response(
                {'msg': "ONLY ADMIN CAN UPDATE"},
                status=status.HTTP_403_FORBIDDEN
            )

        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            return Response(
                CourseSerializer(course).data,
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        if not is_admin(request.user):
            return Response(
                {'msg': "ONLY ADMIN CAN UPDATE"},
                status=status.HTTP_403_FORBIDDEN
            )

        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            course = serializer.save()
            return Response(
                CourseSerializer(course).data,
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not is_admin(request.user):
            return Response(
                {'msg': "ONLY ADMIN CAN DELETE"},
                status=status.HTTP_403_FORBIDDEN
            )

        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
