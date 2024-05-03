resource "aws_ecs_cluster" "clinica_pirmez_process_dev" {
  name = "clinica_pirmez_process_dev"
}

resource "aws_cloudwatch_log_group" "ecs_logs" {
  name = "/ecs/calculo_repasse_dev"
}

resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecs_task_execution_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy_attachment" "ecs_task_execution_ecr_policy_attachment" {
  name       = "ecs_task_execution_ecr_policy_attachment"
  roles      = [aws_iam_role.ecs_task_execution_role.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

resource "aws_iam_policy_attachment" "ecs_task_execution_logs_policy_attachment" {
  name       = "ecs_task_execution_logs_policy_attachment"
  roles      = [aws_iam_role.ecs_task_execution_role.name]
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy" # Política pré-definida que concede permissões para ações necessárias para execução de tarefas do ECS
}

resource "aws_ecs_task_definition" "calculo_repasse_task_definition" {
  family                   = "calculo_repasse_dev"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 256
  memory                   = 512
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  container_definitions    = <<DEFINITION
[
  {
    "name": "calculo_repasse_dev",
    "image": "415953478593.dkr.ecr.us-east-1.amazonaws.com/calculo-repasse:dev",
    "essential": true,
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "${aws_cloudwatch_log_group.ecs_logs.name}",
        "awslogs-region": "us-east-1",
        "awslogs-stream-prefix": "calculo_repasse_dev"
      }
    }
  }
]
DEFINITION
}
