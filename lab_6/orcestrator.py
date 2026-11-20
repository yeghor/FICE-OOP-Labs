"""AKA Lab-6"""

import subprocess

out = subprocess.run("python sp.py2", capture_output=True)
print(f"Subprocess out: {out.stdout}")
print(f"Return code: {out.returncode} Err: {out.stderr}")


sb = subprocess.Popen()
