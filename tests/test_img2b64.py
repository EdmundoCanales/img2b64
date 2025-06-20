from pathlib import Path
from img2b64.img2b64 import img_to_b64


def test_png_output():
    out = img_to_b64(Path("tests/sample.png"))
    assert out.startswith("data:image/png;base64,")


def test_missing_file():
    try:
        img_to_b64(Path("tests/nonexistent.png"))
    except Exception:
        assert True
    else:
        assert False, "Expected an exception for a missing file"
