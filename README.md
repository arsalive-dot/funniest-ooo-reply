# Funniest One-Line Out-of-Office Reply

[![make.fun · u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/arsalive-dot/funniest-ooo-reply/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/arsalive-dot/funniest-ooo-reply/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

An entry for the [Funniest One-Line Out-of-Office Reply](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8) bounty on [make.fun](https://make.fun).

## The reply

> Out of office. I left my inbox in charge and it has already resigned.

One line, 69 characters — under the 160-character gate.

## How it works

`main.py` (Python 3, standard library only) writes the reply to
`/output/entry.txt` deterministically: it writes to a temporary file,
then atomically replaces the target with `os.replace` and sets mode 644.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
