import subprocess
import datetime

container_name = "your_container_name"

def check_container_health():
    try:
        result = subprocess.check_output(
            ["docker", "inspect", "--format={{.State.Health.Status}}", container_name]
        ).decode().strip()
        return result
    except subprocess.CalledProcessError:
        return "not found"

def restart_container():
    subprocess.call(["docker", "restart", container_name])
    print(f"{datetime.datetime.now()}: Restarted {container_name}")

if __name__ == "__main__":
    status = check_container_health()
    if status != "healthy":
        print(f"{datetime.datetime.now()}: {container_name} status = {status}")
        restart_container()
    else:
        print(f"{datetime.datetime.now()}: {container_name} is up and :healthy.")
