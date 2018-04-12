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

## To Do:
- Fix this issue:
* azurerm_virtual_machine.myterraformvm: compute.VirtualMachinesClient#CreateOrUpdate: Failure sending request: StatusCode=400 -- Original Error: autorest/azure: Service returned an error. Status=400 Code="InvalidParameter" Message="Destination path for SSH public keys is currently limited to its default value /home/jah/.ssh/authorized_keys  due to a known issue in Linux provisioning agent."

Terraform does not automatically rollback in the face of errors.
Instead, your Terraform state file has been partially updated with
any resources that successfully completed. Please address the error
above and apply again to incrementally change your infrastructure.


## Doing:
- moving env vars into a secrets file
