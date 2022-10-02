variable "instance_type" {
  type = string

    # condition that checks EC2 instance type
    # must be t2 type to provision resources
    # regex(...) fails if it cannot find a match
  validation {
    condition     = can(regex("^t2.", var.instance_type))
    error_message = "The instance must be a t2 type EC2 instance"
  }
}

