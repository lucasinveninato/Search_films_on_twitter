variable "region" {
  type        = string
  description = "Define what region the instance will be deployed"
  default     = "us-east-1"
}

variable "tags" {
  type        = map(string)
  description = "Tags to set all resources"
  default = {
    Name       = "ec2_instance"
    CustomerID = "customer-id"
    Owner      = "ec2_owner"
  }
}

variable "instance_type" {
  type        = string
  description = "Define the instance type"
  default     = "t2.micro"
}

variable "key_name" {
  type        = string
  description = "Define the key name"
  nullable    = false
}

variable "security_group_name" {
  type        = string
  description = "Define the security group name"
  default     = "security_group"
}

variable "bucket_name" {
  type        = string
  description = "Define the bucket name"
  default     = "security_group"
}

variable "ami" {
  type        = string
  description = "Define the ami"
  default     = "ami-0b0dcb5067f052a63"
}
