#Configuracion de Service Account
resource "google_service_account_key" "my_key" {
    service_account_id = "terraformaccess@proyecto-retodevops.iam.gserviceaccount.com"
    key_algorithm = "KEY_ALG_RSA_2048"
}

