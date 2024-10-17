# Launch the EC2 instance using the existing security group
resource "aws_instance" "worksync_app" {
  ami             = "ami-00f251754ac5da7f0"  # Amazon Linux 2 AMI
  instance_type   = var.instance_type       
  key_name        = var.key_name            

  user_data = file("userdata.sh")  
  tags = {
    Name = "worksync-app"
  }
}
