from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Categoria
from .serializers import CategoriaSerializer
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def listar_categorias(request):
    if request.method == 'GET':
        queryset = Categoria.objects.all()
        serializers =CategoriaSerializer(queryset, many=True)
        return Response(serializers.data)
