import subprocess
import sys
from pathlib import Path
import sys

BIN_NAME = {'linux': 'ffmpeg', 'windows': 'ffmpeg.exe'} [sys.platform]     

ffmpeg = Path(__file__).parent/'external'/sys.platform/BIN_NAME
dest_location = Path('.')/'yt_down'
dest_location.mkdir(exist_ok=True, parents=True)

args = sys.argv[1:]
additional_args = ['--ffmpeg-location', str(ffmpeg)]
if not ('--paths' in args or '-P' in args):
    additional_args.extend(['--paths', str(dest_location)])

subprocess.run(['yt-dlp', *args, *additional_args ])
