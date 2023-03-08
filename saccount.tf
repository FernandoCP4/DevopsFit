#Configuracion de Service Account
resource "google_service_account_key" "my_key" {
    service_account_id = "102037522103560614746"
    key_algorithm = "RSA"
}

