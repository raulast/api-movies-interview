from re import match
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password"
        ]
        read_only_fields = ['email']
        extra_kwargs = {'password': {'write_only': True}}
    

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password_confirmation', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        password = []
        if len(attrs['password']) < 10:
            password.append("It must contain at least 10 characters.")
        if not match(r'(?=.*[A-Z])',attrs['password']):
            password.append("It must contains at least one uppercase letter.")
        if not match(r'(?=.*[a-z])',attrs['password']):
            password.append("It must contains at least one lowercase letter.")
        if not match(r'[!@#?\]]',attrs['password']):
            password.append("It must contains at least one of the following characters: !, @, #, ? or ].")
        if len(password) > 0:
            raise serializers.ValidationError({"password": password})
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password_confirmation": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'] if validated_data.get('first_name') is not None else "",
            last_name=validated_data['last_name'] if validated_data.get('last_name') is not None else "",
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user