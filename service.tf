#Creando el Servicio para el LoadBalancer
resource "kubernetes_service" "my_service" {
    metadata {
        name = "my-service"
    }
    
    spec {
        type = "LoadBalancer"

        selectar = {
            app = "my-app"
        }

        port {
            name = "http"
            port = 80
            target_port = "http"
        }
    }
}