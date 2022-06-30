from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

#First Priority 
#Validators
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name Should be start with R")

class StudentSerialization(serializers.Serializer):
    name = serializers.CharField(max_length=30,validators=[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance

    #Second Priority
    #Field level Validations
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    #Third priority 
    #Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm == 'Rohit' and ct != 'Surat':
            raise serializers.ValidationError("City Must be Surat")
        return data



