import re
import logging
from copy import deepcopy
from rest_framework import serializers
from . import models, helpers
# from . import models, services

class UserSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=False)
	phone = serializers.CharField(required=False)

	class Meta:
		model = models.User
		fields = ['email', 'phone',]
		extra_kwargs = {
			'password': {'write_only': True}
			}
	# def create(self, validated_data):
	# 	data = deepcopy(validated_data)
	# 	user = services.create_user(data)
	# 	return user

	# def update(self, instance, validated_data):
	# 	data = deepcopy(validated_data)
	# 	user = services.update_user(instance, data)
	# 	return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)

class AuthUserSerializer(UserSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ['auth_token']

    def get_auth_token(self, obj):
        return helpers.get_token_for_user(obj, self.context['request'])
        
