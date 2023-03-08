#Configurando Data Source para acceder a repo
data "google_container_registry_image" "my_flask_app" {
  name = "gcr.io/proyecto-retodevops/my-flask-app"
}
