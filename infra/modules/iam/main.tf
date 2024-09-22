data "aws_iam_policy_document" "assume_role" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "role" {
  name               = "${var.role_name}-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

data "aws_iam_policy_document" "lambda_invoke_permission" {
  statement {
    effect = "Allow"
    actions = [
      "lambda:InvokeFunction",
      "secretsmanager:GetSecretValue",
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents",
      "cognito-idp:ConfirmSignUp",
      "cognito-idp:GetUser",
      "cognito-idp:AdminGetUser",
      "cognito-idp:AdminInitiateAuth"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_role_policy" "lambda_invoke_policy" {
  name   = "${var.role_name}-policy"
  role   = aws_iam_role.role.name
  policy = data.aws_iam_policy_document.lambda_invoke_permission.json
}
