# Launch the EC2 instance using the existing security group
resource "aws_instance" "worksync_app" {
  ami             = "ami-00f251754ac5da7f0"  # Amazon Linux 2 AMI
  instance_type   = var.instance_type       # Ensure this variable is defined
  key_name        = var.key_name            # Ensure this variable is defined
  security_groups = ["sg-0419d5d4c4aa6e799"]  # Use the existing security group ID

  user_data = file("userdata.sh")  
  tags = {
    Name = "worksync-app"
  }
}
