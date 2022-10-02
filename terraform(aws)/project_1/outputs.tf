# outputs public iPv4 to cli
output "public_ip" {
  value = aws_instance.my_server.public_ip
}