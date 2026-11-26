"""Write one deterministic UTF-8 line to the requested output directory.
The line turns a 400-word prompt into a concrete complaint: no verb.
"""

import os
from pathlib import Path


LINE = "Your prompt had 400 words and no verb."

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")
if len(LINE) > 200:
    raise ValueError("The entry line must be at most 200 characters.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
