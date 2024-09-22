variable "user_pool_name" {
  type        = string
  description = "Nome do Cognito User Pool"
  default     = "auth-medical-system-user-pool"
}

variable "app_client_name" {
  type        = string
  description = "Nome do Cognito App Client"
  default     = "auth-medical-system-app-client"
}

variable "identity_pool_name" {
  type        = string
  description = "Nome do Cognito Identity Pool"
  default     = "auth-medical-system-identity-pool"
}
