#Definiendo cluster
resource "google_container_cluster" "my_cluster" {
  name               = "my-cluster"
  location           = "us-central1-a"
  initial_node_count = 2
}

#Definiendo los nodos del cluster
resource "google_container_node_pool" "my_pool" {
    name = "my-pool"
    cluster = google_container_cluster.my_cluster.name
    node_count = 2
    node_config {
        machine_type = "n1-standard-1"
    }
}