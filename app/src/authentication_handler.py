import os
import json
import boto3
from aws_lambda_powertools.event_handler.api_gateway import APIGatewayRestResolver, Response, content_types
from src.utils.serialize_document import serialize_document

app = APIGatewayRestResolver(strip_prefixes=["/api"])
cognito_client = boto3.client('cognito-idp')

USER_POOL_ID = os.environ["POOL_ID"]
CLIENT_ID = os.environ["CLIENT_ID"]

@app.post("/signup")
def signup():
    body = app.current_event.json_body
    username = body.get("username")
    password = body.get("password")
    email = body.get("email")
    
    try:
        response = cognito_client.sign_up(
            ClientId=CLIENT_ID,
            Username=username,
            Password=password,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email
                },
                {
                    'Name': 'name',
                    'Value': username
                },
            ]
        )
        return Response(
            status_code=200,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"message": "Usuário cadastrado com sucesso!", "user": response})
        )
    except cognito_client.exceptions.UsernameExistsException:
        return Response(
            status_code=400,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"error": "Usuário já existe!"})
        )
    except Exception as e:
        return Response(
            status_code=500,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"error": str(e)})
        )

@app.post("/confirm-user")
def confirm_user():
    try:
        body = app.current_event.json_body
        username = body.get("username")
        confirmation_code = body.get("confirmation_code")
        
        response = cognito_client.confirm_sign_up(
            ClientId=CLIENT_ID,
            Username=username,
            ConfirmationCode=confirmation_code
        )

        return Response(
            status_code=200,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"message": f"Usuário {username} confirmado com sucesso!"})
        )
    
    except cognito_client.exceptions.UserNotFoundException:
        return Response(
            status_code=404,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"error": "Usuário não encontrado!"})
        )
    except cognito_client.exceptions.CodeMismatchException:
        return Response(
            status_code=400,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"error": "Código de confirmação inválido!"})
        )
    except cognito_client.exceptions.ExpiredCodeException:
        return Response(
            status_code=400,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"error": "Código de confirmação expirado!"})
        )
    except Exception as e:
        return Response(
            status_code=500,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"error": str(e)})
        )

@app.post("/login")
def login():
    body = app.current_event.json_body
    username = body.get("username")
    password = body.get("password")
    
    try:
        response = cognito_client.initiate_auth(
            ClientId=CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        return Response(
            status_code=200,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({
                "message": "Login realizado com sucesso!",
                "tokens": response['AuthenticationResult']
            })
        )
    except cognito_client.exceptions.NotAuthorizedException:
        return Response(
            status_code=401,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"error": "Credenciais inválidas!"})
        )
    except Exception as e:
        return Response(
            status_code=500,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"error": str(e)})
        )

@app.get("/user/<username>")
def get_user(username: str):
    try:
        response = cognito_client.admin_get_user(
            UserPoolId=USER_POOL_ID,
            Username=username
        )
        return Response(
            status_code=200,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"message": "Dados do usuário", "user_data": serialize_document(response)})
        )
    except cognito_client.exceptions.UserNotFoundException:
        return Response(
            status_code=404,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"error": "Usuário não encontrado!"})
        )
    except Exception as e:
        return Response(
            status_code=500,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({"error": str(e)})
        )
