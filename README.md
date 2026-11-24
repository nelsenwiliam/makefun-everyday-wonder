[![make.fun bounty](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/nelsenwiliam/makefun-everyday-wonder/rank.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/nelsenwiliam/makefun-everyday-wonder/reward.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

# Everyday Wonder, Two Days to Find the Line

A single sentence that makes a small everyday moment strange and new: your own shadow reaching the corner ahead of you, looking — just for a second — like it knows exactly where it is going. Written for the make.fun bounty "Everyday Wonder, Two Days to Find the Line".

## Run

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (pure Python stdlib) writes the sentence to `$OUTPUT_DIR/entry.txt` (default `/output`) and verifies it on read-back: one sentence, 1–200 characters, no newline, ending with a period.
