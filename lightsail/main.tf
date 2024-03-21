
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.61.0"
    }
  }
}    
 provider "aws" {
        region = "us-east-1"  
      }

resource "aws_instance" "dev_instances" {
  count         = 2
  ami           = "ami-01eccbf80522b562b"  
  instance_type = "t2.micro"      

  tags = {
    Name = "dev-server${count.index + 1}"
    env  = "dev"
  }
}

resource "aws_instance" "qa_instance" {
  ami           = "ami-01eccbf80522b562b"  
  instance_type = "t2.micro"      

  tags = {
    Name = "qa-server"
    env  = "qa"
  }
}    