 ### Research & Background:
- https://docs.microsoft.com/en-us/azure/virtual-machines/linux/terraform-create-complete-vm
- https://github.com/hashicorp/terraform/issues/9712
- https://www.terraform.io/intro/getting-started/variables.html#from-a-file

### Improvement Ideas & Tasks:
- Enhance the manually configuration environment variable to hold public key for key_data
https://docs.microsoft.com/en-us/azure/virtual-machines/linux/terraform-create-complete-vm#create-virtual-machine
make this secure. For now I will set a password for the user.
- Consider enhancing with [azurerm_key_vault_secret](https://www.terraform.io/docs/providers/azurerm/r/key_vault_secret.html)
- Added Vault integrations such as [vault_generic_secret](https://www.terraform.io/docs/providers/vault/d/generic_secret.html)

## To Run:
- create a secrets var file based on the template
- `$ terraform apply \
  -var-file="secret.tfvars" \
  -var-file="production.tfvars"`
- `terraform apply -var-file=secret.tfvars`
- Obtain the public address `az vm show --resource-group myResourceGroup --name myVM -d --query [publicIps] --o tsv`
- ssh <computer_user>@<address>

## To Do:
- Find out how to validate terraform style and syntax

## Doing:
- moving user & password vars into a secrets file
