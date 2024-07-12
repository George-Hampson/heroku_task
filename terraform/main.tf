terraform {
  required_providers {
    heroku = {
      source  = "heroku/heroku"
      version = "~> 5.2.8"
    }
  }
}

provider "heroku" {
  email   = var.heroku_email
  api_key = var.heroku_api_key
}

resource "heroku_app" "app" {
  name   = var.heroku_app_name
  region = "us"

  config_vars = {
    APP_VERSION = "0.0.4"
    BUILD_DATE  = "2024-07-12"
  }
}

resource "heroku_formation" "web" {
  app_id     = heroku_app.app.id
  type       = "web"
  quantity   = 1
  size       = "Eco"
}
