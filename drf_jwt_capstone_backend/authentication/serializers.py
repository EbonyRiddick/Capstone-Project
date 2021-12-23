from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name')

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
            # If added new columns through the User model, add them in this
            # create method call in the format as seen above
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class SeekerRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        # list as seen below
        # Using existing flag is_staff as "is_owner" to leverage administrative privileges
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'street','city', 'state', 'zip_code')

    def create(self, validated_data):
        #is_owner = validated_data["is_owner"]
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'], 
            street=validated_data['street'],    
            city=validated_data['city'],  
            zip_code=validated_data['zip_code'], 
            state=validated_data['state'],                                     

        )
        user.set_password(validated_data['password'])
        user.save()

        return user
        
class PosterRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User

        fields = ('username', 'password', 'email',
                  'company_name', 'phone_number', 'street','city', 'state', 'zip_code') 

    def create(self, validated_data):
        #is_owner = validated_data["is_owner"]
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            company_name=validated_data['company_name'],
            street=validated_data['street'],    
            city=validated_data['city'],  
            zip_code=validated_data['zip_code'], 
            state=validated_data['state'], 
                                                     
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

