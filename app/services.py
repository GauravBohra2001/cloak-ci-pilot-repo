import subprocess


def run_user_command(cmd: str) -> int:
    return subprocess.run(cmd, shell=True, check=False).returncode
