from django.db.models import Q
from rest_framework import serializers
from .models import Students
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
    # def validate(self, attrs):
    #     if Students.objects.filter(Q(phone=attrs['phone']) | Q(email__iexact=attrs['email'])).exists():
    #         raise serializers.ValidationError('Phone number or email already exists')
    #     return attrs
  
   