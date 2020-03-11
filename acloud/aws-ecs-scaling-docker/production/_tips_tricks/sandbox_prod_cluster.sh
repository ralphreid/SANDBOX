ecs-cli up --capability-iam --security-group ralph_SG_euwest1 --vpc vpc-a4aab4c2 --subnets subnet-20cb5f7a,subnet-6e9dd608,subnet-8a2b71c2 --launch-type FARGATE --cluster production --debug

# Creating Load Balancer
aws elbv2 create-load-balancer --name dockerzon-web --security-groups sg-05db87290dbd96851 --subnets subnet-20cb5f7a subnet-8a2b71c2 subnet-6e9dd608
aws elbv2 create-target-group --name targets-dockerzon --protocol HTTP --port 80 --target-type ip --health-check-protocol HTTP --health-check-port 80 --health-check-path "/health_check" --health-check-timeout-seconds 5 --health-check-interval-seconds 30 --healthy-threshold-count 10 --unhealthy-threshold-count 2 --vpc-id vpc-a4aab4c2
aws elbv2 create-listener --load-balancer-arn arn:aws:elasticloadbalancing:eu-west-1:481461972950:loadbalancer/app/dockerzon-web/00ba132830264b5a --protocol HTTP --port 80 --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:eu-west-1:481461972950:targetgroup/targets-dockerzon/4caf4db04bb50aa0
aws elbv2 modify-load-balancer-attributes --load-balancer-arn arn:aws:elasticloadbalancing:eu-west-1:481461972950:loadbalancer/app/dockerzon-web/00ba132830264b5a --attributes Key=idle_timeout.timeout_seconds,Value=5



# Create CF Dependencies
