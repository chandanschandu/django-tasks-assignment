from django.shortcuts import render

from rest_framework import generics, filters
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_date

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


    def get_queryset(self):
        queryset = Task.objects.all()

        # Sort by date
        if self.request.query_params.get('sort_by_date') == 'true':
            queryset = queryset.order_by('date')

        # Search by date
        search_date = self.request.query_params.get('search_date')
        if search_date:
            parsed_date = parse_date(search_date)
            if parsed_date:
                queryset = queryset.filter(date=parsed_date)

        return queryset

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
