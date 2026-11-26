"""The word you'd delete from the dictionary.

Entry for the make.fun bounty
u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.

The word: "ironic". One word, six characters. Deleting it is
itself ironic — the very word you would need to describe what
just happened is the word that is gone. The humour comes from
the word itself: its meaning, not shock, not a caption. A
reader gets the joke the moment the word is gone, with nothing
explained. It is a real word everyone recognises, spelled
correctly, with nothing added around it — and it is not the
field's obvious pick.

The program writes the single word to /output/entry.txt.
"""

import os

ENTRY = "ironic"


def main() -> None:
    word = ENTRY.strip()
    if not word:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(word) <= 77:
        raise ValueError(f"entry must be 1-77 chars, got {len(word)}")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()

