# Third Party Stuff
import re
import csv
from datetime import datetime, date, timedelta
# from dateutil import tz
from django.contrib.auth import logout
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin,
                                   CreateModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin)

from .response import Response
from rest_framework import status
from first.helpers import MultipleSerializerMixin
from . import models, serializers, helpers
from django.contrib.auth import logout


class AuthViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_classes = {
        'login': serializers.LoginSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = helpers.get_and_authenticate_user(**serializer.validated_data)
        ctx = self.get_serializer_context()
        data = serializers.AuthUserSerializer(user, context=ctx).data
        return helpers.customResponse(data,200,True)

    @action(methods=['GET', ], detail=False, permission_classes=[IsAuthenticated, ])
    def check_token(self, request):
        return helpers.customResponse({"success":True},200,True)

    @action(methods=['POST', ], detail=False, permission_classes=[IsAuthenticated, ])
    def logout(self, request):
        """
        Calls Django logout method; Does not work for UserTokenAuth.
        """
        logout(request)
        return helpers.customResponse({"message": "Successfully logged out."},200,True)