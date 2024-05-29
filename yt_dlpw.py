import subprocess
import sys
from pathlib import Path

ffmpeg = Path(__file__).parent/'external'/'ffmpeg.exe'
dest_location = Path(__file__).parent/'yt_down'
dest_location.mkdir(exist_ok=True, parents=True)

args = sys.argv[1:]
additional_args = ['--ffmpeg-location', str(ffmpeg)]
if not ('--paths' in args or '-P' in args):
    additional_args.extend(['--paths', str(dest_location)])

subprocess.run(['yt-dlp', *args, *additional_args ])