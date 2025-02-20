from rest_framework import serializers

from .models import ToDoNode


class ToDoNodeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ToDoNode
        fields = ('id', 'title', 'description', 'is_done', 'user')