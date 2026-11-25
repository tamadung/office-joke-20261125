"""One-Line Office Joke: writes a single office joke to /output/entry.txt.

The joke is one sentence: a raise request answered with a standing desk,
so the punchline lands on the same pay, just taller.
"""
import os

JOKE = "I asked for a raise and got a standing desk \u2014 now I earn the same money, just taller."


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, one line.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    output_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(JOKE)
    except OSError:
        # Local run fallback: the sandbox always provides /output.
        os.makedirs("out", exist_ok=True)
        with open("out/entry.txt", "w", encoding="utf-8") as f:
            f.write(JOKE)


if __name__ == "__main__":
    main()
