resource "aws_sns_topic" "dead_letter_queue" {
  name = "${var.application}-dlq-${var.environment}"
}
