variable "instance_type" {
  default = "t2.medium"  # Instance size
}

variable "docker_image" {
  default = "umed24/worksync:01"  # Docker image
}

variable "key_name" {
  description = "Key name for SSH access"
  default     = "worksync-key"  # Replace with your actual key pair name
}

variable "region" {
  default = "us-east-1"
}
