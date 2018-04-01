**Idea Sources**:
1. [Microsoft & Terraform](https://docs.microsoft.com/en-us/azure/terraform/)
1. [Scale Sets](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview)
1. [Scale Sets with Networking and Storage](https://docs.microsoft.com/en-us/azure/terraform/terraform-create-vm-scaleset-network-disks-hcl)
1. [Terraform Providers](https://github.com/terraform-providers)

**Build Steps**:
- [ ] Get all connected to azure
  - [Configure Azure Keys Template File](https://github.com/bernadinm/terraform-dcos/blob/master/azure/README.md#configure-your-azure-id-keys)
  - [Setup access to Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/terraform-install-configure#set-up-terraform-access-to-azure)
  - [Configure terraform environment variables](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/terraform-install-configure#configure-terraform-environment-variables)

  `az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/${SUBSCRIPTION_ID}"`
- [ ] Configure & deploy terraform to local machine
- [ ] Make at least one node fire up
- [ ] Fire up a few nodes with networking
- [ ] Configure a Hello World from local to remote machines
- [ ] Configure a Bootstrapper
- [ ] Configure a DCOS Cluster
- [ ] Configure a UCP Cluster
