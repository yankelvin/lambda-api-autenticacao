import json
from src.authentication_handler import app


def lambda_handler(event, context):
    """Handler principal do Lambda que utiliza o APIGatewayRestResolver."""
    return app.resolve(event, context)


# lambda_handler({
#     "path": "/api/signup",
#     "httpMethod": "POST",
#     "body": json.dumps({
#         "username": "teste",
#         "password": "teste123",
#         "email": "teste123@gmail.com"
#     })
# }, None)

# lambda_handler({
#     "path": "/api/login",
#     "httpMethod": "POST",
#     "body": json.dumps({
#         "username": "teste",
#         "password": "teste123"
#     })
# }, None)

# lambda_handler({
#     "path": "/api/user/userId",
#     "httpMethod": "GET"
# }, None)
