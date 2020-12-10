from rest_framework import serializers, status
from .models import Unit, Thread, Task
from .exceptions import ValueException

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("input",)

    def validate_input(self, input):
        try:
            print(input)
            if int(input) < 0:
                raise ValueException(detail={"Error": "Only positive integers allowed"}, status_code=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            raise ValueException(detail={"Error": "Non integer value"}, status_code=status.HTTP_400_BAD_REQUEST)
        return input

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'