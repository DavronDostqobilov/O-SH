from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

# CREATE va LIST
@api_view(['GET', 'POST'])
def person_list_create(request):
    if request.method == 'GET':  # READ (hamma odamlarni olish)
        users = Person.objects.all()
        serializer = PersonSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':  # CREATE (yangi odam qo'shish)
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# RETRIEVE, UPDATE va DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':  # RETRIEVE (bitta odamni olish)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    
    elif request.method == 'PUT':  # UPDATE (ma'lumotni yangilash)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':  # DELETE (o'chirish)
        person.delete()
        return Response({'message': 'Person deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
