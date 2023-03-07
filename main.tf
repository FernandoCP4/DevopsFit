provider "google" {
  project = "proyecto-retodevops"
  region  = "us-central1"
}

provider "kubernetes" {
  config_context_cluster = "my-k8s-cluster"
}

resource "google_container_cluster" "my-cluster" {
  name     = "my-k8s-cluster"
  location = "us-central1"

  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }

  node_pool {
    name             = "default-node-pool"
    machine_type     = "n1-standard-1"
    initial_node_count = 1
  }
}

resource "kubernetes_deployment" "my-app" {
  metadata {
    name = "my-app"
  }

  spec {
    replicas = 3

    selector {
      match_labels = {
        app = "my-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "my-app"
        }
      }

      spec {
        container {
          image = "gcr.io/my-project/my-app:latest"
          name  = "my-app"
          port {
            container_port = 80
          }
        }
      }
    }
  }
}
