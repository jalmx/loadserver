from paramiko import SSHClient
from scp import SCPClient
import sys


# Define progress callback that prints the current percentage completed for the file


def progress(filename, size, sent):
    sys.stdout.write("%s's progress: %.2f%%   \r" %
                     (filename, float(sent) / float(size) * 100))


ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('openmediavault.local', username="josef", password="1234", timeout=5)

scp = SCPClient(ssh.get_transport(), progress=progress)

scp.put("/home/xizuth/Downloads/cb85/video promocion mecatronica85 2022.mp4",
        "/srv/dev-disk-by-uuid-ba6e350a-33b7-4323-b908-dde405739b13/test")

scp.close()
