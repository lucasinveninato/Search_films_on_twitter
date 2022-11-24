instance_type       = "t2.medium"
key_name            = "ssh-key-tweetstop10"
security_group_name = "terraform-sg-twitter-search"
bucket_name         = "top-10-actors-tweets"
ami = "ami-0b0dcb5067f052a63" #Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type 
tags = {
  Name       = "top-10-actors-tweets-instance"
  CustomerID = ""
  Owner      = ""
}