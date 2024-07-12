output "heroku_app_url" {
  description = "URL of the Heroku app"
  value       = "https://${heroku_app.app.name}.herokuapp.com"
}
