# Third Party Stuff
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from django.utils.module_loading import import_string
from rest_framework.response import Response

TOKEN_BACKEND_SERVICE_CLASS = import_string(settings.TOKEN_BACKEND_SERVICE)


class MultipleSerializerMixin(object):
    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(MultipleSerializerMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @list_route
            def my_action:
                ...

        If there's no serializer available for that action than
        the default serializer class will be returned as fallback.
        """
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise exc.WrongArguments("Invalid username/password. Please try again!")
    return user

def get_user_for_token(token, *args, **kwargs):
    return TOKEN_BACKEND_SERVICE_CLASS().get_user_for_token(token, *args, **kwargs)


def get_token_for_user(user, *args, **kwargs):
    return TOKEN_BACKEND_SERVICE_CLASS().get_token_for_user(user, *args, **kwargs)

def customResponse(data,status_code,success):
    if success:
        return Response(data=data,status=status_code)
    else:
        error_data = {
            "error":{
                "code":status_code,
                "message":data
            }
        }
        return Response(data=error_data,status=status_code)

