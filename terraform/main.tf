
# Create a new security group with a unique name
resource "aws_security_group" "new_allow_http_ssh" {
  name        = "new_allow_http_ssh"  # Change the name to something unique
  description = "Allow inbound HTTP, SSH, and application traffic"
  vpc_id      = "vpc-067575f1870e8da0d"  # Ensure this VPC ID is correct

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 1000
    to_port     = 1000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Launch the EC2 instance using the newly created security group
resource "aws_instance" "worksync_app" {
  ami             = "ami-00f251754ac5da7f0"  # Amazon Linux 2 AMI
  instance_type   = var.instance_type       # Ensure this variable is defined
  key_name        = var.key_name            # Ensure this variable is defined
  security_groups = [aws_security_group.new_allow_http_ssh.name]  # Use the new security group

  user_data = file("userdata.sh")  
  tags = {
    Name = "worksync-app"
  }
}
