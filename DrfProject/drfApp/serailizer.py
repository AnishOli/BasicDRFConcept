from rest_framework import serializers

class TeacherSerializer(serializers.Serializer):
    name= serializers.CharField()
    age= serializers.IntegerField()
    email=serializers.EmailField()