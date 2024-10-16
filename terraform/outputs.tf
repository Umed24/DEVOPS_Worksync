output "instance_public_ip" {
  value = aws_instance.worksync_app.public_ip
}
