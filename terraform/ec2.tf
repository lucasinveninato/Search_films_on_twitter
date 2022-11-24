resource "aws_instance" "server" {
  ami             = var.ami
  instance_type   = var.instance_type
  key_name        = aws_key_pair.tf_key.key_name
  security_groups = ["${aws_security_group.security_group.name}"]
  tags            = var.tags
}

resource "tls_private_key" "pk" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "tf_key" {
  key_name   = var.key_name
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "local_file" "ssh_key" {
  filename = "${aws_key_pair.tf_key.key_name}.pem"
  content = tls_private_key.pk.private_key_pem
}