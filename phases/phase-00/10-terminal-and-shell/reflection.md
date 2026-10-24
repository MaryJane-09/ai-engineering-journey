# SE 00 Lesson 10: Reflection

## Learner reflection

The learner explained that redirecting with `> output.log 2>&1` captures both normal output and errors. Their grep/awk pipeline extracted the loss values `0.8`, `0.4`, and `0.2`. They were unsure about tmux and chose an incorrect SSH port-forwarding command.

## Takeaway

`>` sends command output to a file; `|` sends it into another command. `tmux` lets you return to a live terminal session, while `ssh -L` forwards a remote service port to a local port.

## Question to revisit

What is the difference between detaching from a tmux session and closing the terminal that started a regular command?
