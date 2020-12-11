from rest_framework import serializers, status
from .models import Unit, Thread, Task
from .exceptions import ValueException


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("input",)

    def validate_input(self, input):
        try:
            if int(input) < 0:
                raise ValueException(detail={"Error": "Only positive integers allowed"},
                                     status_code=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            raise ValueException(detail={"Error": "Non integer value"}, status_code=status.HTTP_400_BAD_REQUEST)
        return input

class TaskCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'output',)

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UnitListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class ThreadViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

class UnitRegisterSerializer(serializers.ModelSerializer):
    threads = serializers.IntegerField(write_only=True, min_value=1, max_value=16)

    class Meta:
        model = Unit
        fields = ('port', 'threads',)


class UnitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('ip', 'port',)
