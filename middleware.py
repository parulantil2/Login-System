import logging
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_authentication = JWTAuthentication()

    def __call__(self, request):
        # Extract the token from the request
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]  # Remove 'Bearer ' prefix
            try:
                # Authenticate the token
                validated_token = self.jwt_authentication.get_validated_token(token)
                user = self.jwt_authentication.get_user(validated_token)
                request.user = user
            except (InvalidToken, TokenError):
                request.user = None
        else:
            request.user = None

        response = self.get_response(request)
        return response
