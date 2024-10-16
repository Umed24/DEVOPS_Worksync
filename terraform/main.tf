data "aws_security_group" "allow_http_ssh" {
  vpc_id = "vpc-067575f1870e8da0d"

  filter {
    name   = "group-name"
    values = ["allow_http_ssh"]
  }
}

resource "aws_security_group" "allow_http_ssh" {
  count = length(data.aws_security_group.allow_http_ssh.id) == 0 ? 1 : 0  # Changed from ids to id

  name        = "allow_http_ssh"
  description = "Allow inbound HTTP, SSH, and application traffic"

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

resource "aws_instance" "worksync_app" {
  ami             = "ami-00f251754c5da7f0"  # Amazon Linux 2 AMI
  instance_type   = var.instance_type
  key_name        = var.key_name
  security_groups = [aws_security_group.allow_http_ssh[0].name]  # Use index [0] for the created security group

  user_data = file("userdata.sh")  
  tags = {
    Name = "worksync-app"
  }
}
