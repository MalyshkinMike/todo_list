from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import ToDoNode
from .permissions import IsOwnerOrAdmin
from .serializers import ToDoNodeSerializer

class ToDoAPIList(ListCreateAPIView):
    serializer_class = ToDoNodeSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return ToDoNode.objects.all()
        return ToDoNode.objects.filter(user=self.request.user.pk)




class ToDoAPIRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = ToDoNode.objects.all()
    serializer_class = ToDoNodeSerializer
    permission_classes = (IsOwnerOrAdmin, )

class ToDoAPIDelete(DestroyAPIView):
    queryset = ToDoNode.objects.all()
    serializer_class = ToDoNodeSerializer
    permission_classes = (IsOwnerOrAdmin, )