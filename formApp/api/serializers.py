from pyexpat import model
from formApp.models import addStd
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = addStd
        fields = ['stdId', 'stdName', 'stdEmail', 'stdPassword']