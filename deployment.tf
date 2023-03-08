#Kubernetes deployment
resource "kubernetes_deployment" "my_deployment" {
    metadata {
        name = "my-deployment"
    }

    spec {
        selector {
            match_labels = {
                app = "my-flask-app"
            }
        }
        
        replicas = 2

        template {
            metadata {
                labels = {
                    app = "my-flask-app"
                }
            }

            spec {
                container {
                    image = data.google_container_registry_image.my_flask_app.name
                    name = "my-flask-app"
                }
            }
        }
    }
}