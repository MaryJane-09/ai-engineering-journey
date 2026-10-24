# SE 00 Lesson 10: Filter a Training Log

## Goal

Use a redirect to save a small log, then pipe it through `grep` and `awk` to extract loss values.

## Procedure

Run these commands in a terminal:

```bash
printf 'epoch 1 loss: 0.8\nepoch 2 loss: 0.4\nepoch 3 loss: 0.2\n' > /tmp/fake-train.log
grep 'loss:' /tmp/fake-train.log | awk '{print $NF}'
```

The first command writes three lines to a temporary file. The second filters matching lines and prints each line's last field.

## Expected output

```text
0.8
0.4
0.2
```

## Observed result

The learner's pipeline printed:

```text
0.8
0.4
0.2
```

## Remaining evidence

The learner explained that `>` redirects command output to a file, while `|` sends one command's output to the next command as input.

**Status: Complete.** The log values were extracted, and the learner distinguished file redirection from a command pipeline.
