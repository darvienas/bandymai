from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    employees = serializers.StringRelatedField(many=True)
    tasks = serializers.StringRelatedField(many=True)
    bills = serializers.StringRelatedField(many=True)
    # boss = serializers.ReadOnlyField(source='user.username')
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date', 'client', 'boss', 'employees', 'tasks', 'bills', 'user_id', 'user']
        # fields = '__all__'

    
# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password', 'password2')
#         extra_kwargs = {'password':{'write_only':True}, 'password2':{'write_only':True}}

#     def create(self, validated_data):
        
#         user = User.objects.create(**validated_data) # user = User(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    

# #Serializer to Get User Details using Django Token Authentication
# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = ["id", "first_name", "last_name", "username"]


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
            'email', 'first_name', 'last_name')
        extra_kwargs = {
        'first_name': {'required': True},
        'last_name': {'required': True}
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
  
  # CHAT GPT
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user