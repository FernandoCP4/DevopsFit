#Creando el Servicio para el LoadBalancer
resource "kubernetes_service" "my_service" {
    metadata {
        name = "my-service"
    }
    
    spec {
        type = "LoadBalancer"

        selector = {
            app = "my-app"
        }

        port {
            name = "http"
            port = 80
            target_port = "http"
        }
    }
}