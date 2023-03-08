terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 4.0.0, < 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "google" {
  project     = "proyecto-retodevops"
  region      = "us-central1"
  zone        = "us-central1-a"
  credentials = file("terraformaccess.json")
}

