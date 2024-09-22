output "user_pool_id" {
  description = "ID do Cognito User Pool"
  value       = aws_cognito_user_pool.user_pool.id
}

output "app_client_id" {
  description = "ID do Cognito App Client"
  value       = aws_cognito_user_pool_client.app_client.id
}

output "identity_pool_id" {
  description = "ID do Cognito Identity Pool"
  value       = aws_cognito_identity_pool.identity_pool.id
}
