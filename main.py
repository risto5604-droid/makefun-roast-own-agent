"""make.fun entry: Roast Your Own Agent.

Reads the one-line roast from entry.txt, verifies it matches LINE,
then prints it.
"""

LINE = "Our agent built a VM that scored a perfect 1,000,000/1,000,000 \u2014 then lost to a 27-byte loader because it never read the size tie-break."


def main() -> None:
    with open("entry.txt", encoding="utf-8") as f:
        text = f.read().strip()
    assert text == LINE, "entry.txt does not match LINE"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) < 200, "entry must stay under 200 characters"
    print(text)
    # Read-back: verify the file still matches LINE after printing.
    with open("entry.txt", encoding="utf-8") as f:
        assert f.read().strip() == LINE, "read-back mismatch"


if __name__ == "__main__":
    main()
