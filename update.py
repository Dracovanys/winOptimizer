import subprocess
import os

subprocess.call(f'git -C {os.path.dirname(os.path.realpath(__file__))} pull')