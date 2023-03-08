provider "google" {
  project     = "proyecto-retodevops"
  region      = "us-central1"
  zone        = "us-central1-a"
  credentials = file(terraformaccess.json)

  required_providers {
  google = {
    source  = "registry.terraform.io/hashicorp/google"
    version = ">= 4.0.0, < 5.0"
  }
  kubernetes = {
    source  = "registry.terraform.io/hashicorp/kuberenetes"
    version = "~> 2.0"
  }
}
}

