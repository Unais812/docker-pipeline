resource "aws_instance" "this" {
    ami = "ami-0f50f13aefb6c0a5d"
    instance_type = "t3.micro"
    tags = {
        Name = "terraform create"
    }
    user_data_replace_on_change = false
}
