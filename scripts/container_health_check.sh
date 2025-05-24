#!/bin/bash

container_name="your_container_name"
health=$(docker inspect --format='{{.State.Health.Status}}' "$container_name" 2>/dev/null)

if [ "$health" != "healthy" ]; then
  echo "$(date): $container_name is unhealthy. Restarting..."
  docker restart "$container_name"
else
  echo "$(date): $container_name is healthy."
fi
