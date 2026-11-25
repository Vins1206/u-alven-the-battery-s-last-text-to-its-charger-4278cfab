from pathlib import Path

TEXT = "u up? it's 1%. I waited all day while you charged your watch, your vape, and your AirPods. I get it, I'm the side battery. I'm dying now — and I'm taking your 6am alarm with me."

OUTPUT = Path("/output/entry.txt")

assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "entry must be 1-200 chars"

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(TEXT, encoding="utf-8")
