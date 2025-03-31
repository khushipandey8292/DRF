from rest_framework import serializers
from .models import Student1

def start_with_k(value):
    if value[0].lower()!='k':
        raise serializers.ValidationError('name should be start with k')
    
class Student1Serializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[start_with_k])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
    def create(self,validated_data):
        return Student1.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
# Field lavel validation

    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seat full')
        return value
# object level validation   
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='ravi' and ct.lower()!='dhanbad':
            raise serializers.ValidationError('city must be Dhanbad')
        return data