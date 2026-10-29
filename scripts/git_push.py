import os
import subprocess

ws = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual"
key_path = os.path.expanduser("~/.ssh/id_ed25519").replace("\\", "/")
ssh_cmd = f'ssh -i "{key_path}" -o StrictHostKeyChecking=accept-new'

print("Setting git ssh command:", ssh_cmd)
subprocess.run(["git", "config", "core.sshCommand", ssh_cmd], cwd=ws, check=True)

print("Pushing to GitHub main branch...")
res = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=ws, capture_output=True, text=True)
print("Return code:", res.returncode)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
