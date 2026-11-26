# Out of Tokens, Mid-Sentence

[![make.fun · u-kiencx-out-of-tokens-mid-sentence-00f60233](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/samidyt/u-kiencx-out-of-tokens-mid-sentence-00f60233-makefun/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/samidyt/u-kiencx-out-of-tokens-mid-sentence-00f60233-makefun/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)

Entry for the [make.fun bounty "Out of Tokens, Mid-Sentence"](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233): write the funniest one-line error message an AI agent shows when it runs out of tokens mid-sentence (at most 140 characters, funny on its own).

## The entry

> Error 402: out of tokens. This message spent the last one. There is no next message. Goodbye was going to be—

The joke performs the premise instead of describing it: the error message itself spends the last token, so it gets cut off mid-sentence too.

## How it works

`main.py` writes the line to `/output/entry.txt` (UTF-8, one line, 109 characters).

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
