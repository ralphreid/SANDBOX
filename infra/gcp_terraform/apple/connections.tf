provider "google" {
  credentials = "${file("account.json")}"
  project     = "apple-124"
  region      = "us-west1"
}
