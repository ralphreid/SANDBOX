variable arm_subscription_id {}
variable arm_client_id {}
variable arm_client_secret {}
variable arm_tenant_id {}

variable ssh_public_key_file {
  description = "ssh public key"
  default     = "~/.ssh/id_rsa.pub"
}
