from rest_framework import serializers
from .models import Teacher
import re

class TeacherSerializer(serializers.Serializer):
    name= serializers.CharField()
    age= serializers.IntegerField()
    email=serializers.EmailField()
    phone=serializers.CharField()
    
    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
    
    # validation of the data using searializer
    
    def validate_age(self, age):
        if age>100 or age<0:
            raise serializers.ValidationError("Age should be between 1 to 100")
        return age
    def validate_phone(self, phone):
        if not re.match(r"^(98|97)\d{8}$",phone):
            raise serializers.ValidationError("Invalid phone number")
        return phone
    def validate_email(self, email):
        if not email.endswith("@gmail.com"):
            raise serializers.ValidationError("Invalid email")
        return email
    
    """This is for updating whole data  in database"""
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.email=validated_data.get('email',instance.email)
        instance.phone=validated_data.get('phone',instance.phone)
        instance.save()
        return instance
    
    

class ProductSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    price=serializers.IntegerField()
    desc=serializers.CharField()