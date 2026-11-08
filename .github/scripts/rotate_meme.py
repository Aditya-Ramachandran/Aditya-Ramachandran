from pathlib import Path
import re
import secrets


README = Path("README.md")
START = "<!-- rotating-meme:start -->"
END = "<!-- rotating-meme:end -->"

# Curated developer GIFs from GIPHY. Keep this list small enough that every
# rotation still feels like it belongs on the profile.
MEMES = (
    "QX6ruFElzFdeIfblrg",  # pixel-art coding
    "1iNIkQBAwEkUuTpikf",  # code loading
    "mTPjPA6SSXgTsnZ1Dh",  # code not working
    "WDJBtnl2cxgReYekEu",  # web development
    "9t9WIiEDUWxiYRWDBz",  # works on my machine
)


def render(meme_id: str) -> str:
    return f'''{START}
<div align="center" data-meme-id="{meme_id}">
  <a href="https://giphy.com/gifs/{meme_id}">
    <img src="https://media.giphy.com/media/{meme_id}/giphy.gif" width="520" alt="Rotating developer meme">
  </a>
  <br>
  <sub>Today's build mood. Shuffled daily.</sub>
</div>
{END}'''


text = README.read_text(encoding="utf-8")
start = text.index(START)
end = text.index(END, start) + len(END)
current_block = text[start:end]
current_match = re.search(r'data-meme-id="([^"]+)"', current_block)
current = current_match.group(1) if current_match else None

choices = [meme_id for meme_id in MEMES if meme_id != current]
next_meme = secrets.choice(choices or list(MEMES))

README.write_text(text[:start] + render(next_meme) + text[end:], encoding="utf-8")
print(f"Rotated profile meme: {current or 'unknown'} -> {next_meme}")
