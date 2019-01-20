## Steps:
- Setup up service account
- Get keys
- enable GKE & Billing
- gcloud projects add-iam-policy-binding apple-124 --member "serviceAccount:terraform@apple-124.iam.gserviceaccount.com" --role roles/container.admin
- gcloud projects add-iam-policy-binding apple-124 --member "serviceAccount:terraform@apple-124.iam.gserviceaccount.com" --role roles/iam.serviceAccountUser
- roles/compute.admin
