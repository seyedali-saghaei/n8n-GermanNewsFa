import argparse
import subprocess
import tempfile
from pathlib import Path


def merge_videos(video_files, output_file):
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".txt",
        delete=False,
        encoding="utf-8"
    ) as f:

        for video in video_files:
            f.write(f"file '{Path(video).as_posix()}'\n")

        list_file = f.name

    command = [
        "ffmpeg",
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        list_file,
        "-c",
        "copy",
        str(output_file),
    ]

    print("Running:")
    print(" ".join(command))

    result = subprocess.run(command)

    if result.returncode != 0:
        raise RuntimeError("FFmpeg merge failed.")

    print()
    print("Video merged successfully:")
    print(output_file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--output",
        required=True,
    )

    parser.add_argument(
        "videos",
        nargs="+",
    )

    args = parser.parse_args()

    merge_videos(
        args.videos,
        args.output,
    )