import secrets
import base64

# For Django Use THe Following Code 
# Python manage.py shell
# from django.core.management.utils import get_random_secret_key 
# django_sec = get_random_secret_key()
# print (django_sec)

# Generate a random byte sequence and encode it in base64
jwt_secret_key = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode('utf-8')

print(jwt_secret_key)
