from django.shortcuts import render,get_object_or_404
from .serializers import BatchSerializer
from .models import Batch
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

def is_admin(user):
    return user.is_authenticated and getattr(user,"role",None)=="ADMIN"

class BatchListApi(APIView):

    def get(self,request):
        batches = Batch.objects.all()
        serializers =BatchSerializer(batches,many=True)
        return Response(
            serializers.data,
            status = status.HTTP_200_OK
        )
    
    def post(self,request):
        if not is_admin(request.user):
            return Response({
                'msg':"ONLY ADMIN CAN ADD THE BATCHES"},
                status = status.HTTP_403_FORBIDDEN
            )
        serializer =BatchSerializer(data=request.data)
        if serializer.is_valid():
            batch = serializer.save()
            return Response(
                BatchSerializer(batch).data,
                status = status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

class BatchDetailsAPI(APIView):
    # CRUD operations
    def get_object(self,pk):
        return get_object_or_404(Batch,pk=pk)
    
    def get(self,request,pk):
        batch = self.get_object(pk)
        serializer = BatchSerializer(batch)
        return Response(
            serializer.data,
            status = status.HTTP_200_OK
        )

    def put(self,request,pk):
        if not is_admin(request.user):
            return Response(
                {'msg':"ONLY ADMIN CAN UPDATE THE CHANGES"},
                status = status.HTTP_403_FORBIDDEN
            )
        batch = self.get_object(pk)
        serializer = BatchSerializer(batch , data=request.data)
        if serializer.is_valid():
            batch = serializer.save()
            return Response(
                BatchSerializer(batch).data,
                status =status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        ) 
    
    def patch(self,request,pk):
        if not is_admin(request.user):
            return Response(
                {'msg':"ONLY ADMIN CAN UPDATE THE CHANGES"},
                status = status.HTTP_403_FORBIDDEN
            )
        batch = self.get_object(pk)
        serializer = BatchSerializer(batch,data= request.data)
        if serializer.is_valid():
            batch = serializer.save()
            return Response(
                BatchSerializer(batch).data,
                status =status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    def delete(self,request,pk):
        if not is_admin(request.user):
            return Response(
                {'msg':"ONLY USER CAN DELETE THE BATCH"},
                status =status.HTTP_403_FORBIDDEN
            )
        batch = self.get_object(pk)
        batch.delete()
        return Response(
            status = status.HTTP_204_NO_CONTENT
        )