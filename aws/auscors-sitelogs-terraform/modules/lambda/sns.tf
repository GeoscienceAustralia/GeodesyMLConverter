resource "aws_sns_topic" "dead_letter_queue" {
  name = "${var.application}-dlq-${var.environment}"
}

output "dead_letter_queue_arn" {
  value = "${aws_sns_topic.dead_letter_queue.arn}"
}
