module "iam" {
  source    = "./modules/iam"
  role_name = "lambda-api-autenticacao"
}

module "cognito" {
  source             = "./modules/cognito"
  user_pool_name     = "auth-medical-system-user-pool"
  app_client_name    = "auth-medical-system-app-client"
  identity_pool_name = "auth-medical-system-identity-pool"
}

module "lambda" {
  source        = "./modules/lambda"
  function_name = "lambda-api-autenticacao"
  role_arn      = module.iam.role_arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  memory_size   = 256
  timeout       = 29

  environment_variables = {
    POOL_ID   = module.cognito.user_pool_id
    CLIENT_ID = module.cognito.app_client_id
  }

  depends_on = [module.iam, module.cognito]
}
