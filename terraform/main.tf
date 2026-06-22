provider "aws" {
  region = "us-east-1"
}

resource "aws_wafv2_ip_set" "practice" {
  name               = "tf-practice"
  scope              = "CLOUDFRONT"
  ip_address_version = "IPV4"
  addresses          = ["192.0.2.0/24"]
  description        = "Terraform practice IP set - safe to delete"
}