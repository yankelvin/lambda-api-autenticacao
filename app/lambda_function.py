import json
from src.authentication_handler import app


def lambda_handler(event, context):
    """Handler principal do Lambda que utiliza o APIGatewayRestResolver."""
    return app.resolve(event, context)


# lambda_handler({
#     "path": "/api/signup",
#     "httpMethod": "POST",
#     "body": json.dumps({
#         "username": "teste-cognito",
#         "password": "Teste@123",
#         "email": "teste-cognito@mailinator.com"
#     })
# }, None)

# lambda_handler({
#     "path": "/api/confirm-user",
#     "httpMethod": "POST",
#     "body": json.dumps({
#         "username": "teste-cognito",
#         "confirmation_code": "475454"
#     })
# }, None)

# lambda_handler({
#     "path": "/api/login",
#     "httpMethod": "POST",
#     "body": json.dumps({
#         "username": "teste-cognito",
#         "password": "Teste@123"
#     })
# }, None)

# lambda_handler({
#     "path": "/api/user/teste-cognito",
#     "httpMethod": "GET",
#     "queryStringParameters": {
#     }
# }, None)
