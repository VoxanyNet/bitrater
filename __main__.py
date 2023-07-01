import os
import argparse
import sys

parser = argparse.ArgumentParser(description='Get appropriate bitrate for video given desired file size')

parser.add_argument('video_path', help='path to video file')
parser.add_argument('target_size', help='the target file size to calculate for')

args = parser.parse_args()

video_path: str = args.video_path
target_size: str = args.target_size

if os.path.exists(video_path) != True:
    print(f"Could not find {video_path}")
    sys.exit(1)

video_info = os.system(f"ffmpeg -i {video_path}")