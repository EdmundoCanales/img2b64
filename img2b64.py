import argparse, base64, sys
from pathlib import Path


def img_to_b64(path: Path) -> str:
    """Convert an image file to a base64 encoded string."""
    data = path.read_bytes()
    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }.get(path.suffix.lower(), "application/octet-stream")
    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:{mime};base64,{b64}"


def main():
    p = argparse.ArgumentParser(
        description="Convert an image file to a Markdown‐embedded Base64 string."
    )
    p.add_argument("input", type=Path, help="Path to the image file.")
    p.add_argument(
        "-o", "--output", type=Path, help="write MD snippet to a file (default=stdout)"
    )
    args = p.parse_args()

    try:
        snippet = f"![{args.input.stem}]({img_to_b64(args.input)})"
        if args.output:
            args.output.write_text(snippet, encoding="utf-8")
            print(f"Markdown snippet written to {args.output}")
        else:
            print(snippet)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
