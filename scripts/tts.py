import argparse
import asyncio
import base64
import sys
from pathlib import Path

import edge_tts


async def generate_speech(
    text: str,
    output: Path,
    voice: str,
    rate: str,
    pitch: str,
) -> None:
    text = text.strip()

    if not text:
        raise ValueError("TTS text is empty.")

    output.parent.mkdir(parents=True, exist_ok=True)

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate,
        pitch=pitch,
    )

    await communicate.save(str(output))


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Persian audio with Edge TTS."
    )

    text_group = parser.add_mutually_exclusive_group(required=True)

    text_group.add_argument(
        "--text",
        help="Plain UTF-8 text.",
    )

    text_group.add_argument(
        "--text-base64",
        help="UTF-8 text encoded as Base64.",
    )

    parser.add_argument("--output", required=True)

    parser.add_argument(
        "--voice",
        default="fa-IR-FaridNeural",
    )

    parser.add_argument(
        "--rate",
        default="-5%",
    )

    parser.add_argument(
        "--pitch",
        default="-2Hz",
    )

    return parser.parse_args()


def resolve_text(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text

    try:
        decoded_bytes = base64.b64decode(
            args.text_base64,
            validate=True,
        )

        return decoded_bytes.decode("utf-8")

    except Exception as error:
        raise ValueError(
            f"Invalid Base64 TTS text: {error}"
        ) from error


async def main() -> None:
    args = parse_arguments()
    output_path = Path(args.output).resolve()

    try:
        text = resolve_text(args)

        await generate_speech(
            text=text,
            output=output_path,
            voice=args.voice,
            rate=args.rate,
            pitch=args.pitch,
        )

        print(f"TTS_SUCCESS:{output_path}")

    except Exception as error:
        print(f"TTS_ERROR:{error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())