# Infrastructure Monitoring & Auto-Healing on GCP

This project sets up container health monitoring using Prometheus and Grafana, with auto-healing logic using Bash/Python scripts.

## Tech Stack
- GCP Compute Engine (Linux VM)
- Docker
- Prometheus & Grafana
- Bash & Python scripting
- Alertmanager (optional)

## Structure
- `scripts/`: Health check + restart automation
- `prometheus/`: Prometheus config + alert rules
- `grafana/`: Exported dashboard (JSON)
- `docs/`: Diagrams, documentation

## Usage
1. Deploy Prometheus and Grafana
2. Set up health checks for Docker containers
3. Use cron to run `container_health_check.sh` or `auto_restart.py` periodically
4. Monitor dashboards and alerts

## License
MIT
