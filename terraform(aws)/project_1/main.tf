# declare aws provider in terraform block
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.26.0"
    }
  }
}

# move .tfstate file to cloud
terraform {
  cloud {
    organization = "org-name"

    workspaces {
      name = "workspace-name"
    }
  }
}

# ec2 instance resource block
resource "aws_instance" "my_server" {
  ami                    = "ami-0fb391cce7a602d1f"
  instance_type          = var.instance_type
  availability_zone      = "eu-west-2a"
  key_name               = "access_key"
  vpc_security_group_ids = [aws_security_group.sg_my_server.id]
  user_data              = data.template_file.user_data.rendered

  tags = {
    Name = "My_Server"
  }
}

# s3 bucket resource block
resource "aws_s3_bucket" "bucket" {
  bucket = "34324908329048-depends-on"
  depends_on = [
    aws_instance.my_server
  ]
}

# s3 bucket1 resource block
resource "aws_s3_bucket" "bucket1" {
  bucket = "my-new-bucket-234324325"
}

# data block to read userdata.yml file
# enables apache2
data "template_file" "user_data" {
  template = file("./userdata.yml")
}

data "aws_vpc" "main" {
  id = "vpc-057ff9f588c8afa8e"
}

# local values to be referenced in dynamic block
# HTTP and SSH
locals {
  ingress_rules = [{
    port        = 80
    description = "HTTP from VPC"
    },
    {
      port        = 22
      description = "SSH"
  }]
}

# resource block for security group
resource "aws_security_group" "sg_my_server" {
  name        = "sg_my_server"
  description = "MyServer_SG"
  vpc_id      = data.aws_vpc.main.id

  # dynamic block to reduce no. of times code is repeated
  dynamic "ingress" {
    for_each = local.ingress_rules

    content {
      description      = ingress.value.description
      from_port        = ingress.value.port
      to_port          = ingress.value.port
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
    }

  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1" #Any protocol
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
  tags = {
    Name = "allow_web"
  }
}

# module block to create public and private subnets
# across multiple availability zones
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-2a", "eu-west-2b", "eu-west-2c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}

