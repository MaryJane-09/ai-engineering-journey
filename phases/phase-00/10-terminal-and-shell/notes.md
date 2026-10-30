# SE 00 Lesson 10: Terminal & Shell

These notes summarize the [official Terminal & Shell lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/10-terminal-and-shell). The small log pipeline exercise is complete; see [`experiment.md`](experiment.md).

## Terminal and shell

The terminal is the interface where you type commands. The shell (such as `zsh` or `bash`) reads those commands, expands arguments, and starts programs. This workspace uses `zsh`.

## Pipes and redirects

- A pipe `|` sends one command's standard output into the next command's standard input. For example, `grep 'loss:' train.log | awk '{print $NF}'` filters loss lines, then prints the last field from each line.
- `>` sends standard output to a file and replaces that file's previous contents.
- `>>` appends standard output to a file.
- `2>` sends standard error to a file.
- `2>&1` sends standard error to the same destination as standard output. Thus `python train.py > output.log 2>&1` captures both normal output and errors in `output.log`.

## Long-running jobs

`command &` starts a background job but it usually ends when its terminal closes. `nohup command > run.log 2>&1 &` can survive terminal closure and writes to a log, but you cannot reattach to its live terminal. `tmux` keeps a persistent terminal session: detach with `Ctrl+B`, then `d`; later reconnect with `tmux attach -t <name>` and see live output. `tmux` is not installed in this environment, so no tmux exercise was run.

## Remote work

- `ssh user@host` opens a remote shell.
- `scp` copies files over SSH; `rsync` efficiently syncs directories.
- `ssh -L 8888:localhost:8888 user@gpu-box` forwards local port 8888 to port 8888 on the remote host. Open `localhost:8888` locally to reach the remote Jupyter service.

## Learner evidence and review

The learner correctly explained that `> output.log 2>&1` captures both normal output and errors. Their log pipeline printed `0.8`, `0.4`, and `0.2`. They then summarized the distinction: `>` redirects output to a file, while `|` sends the first command's output to the next command as input. In review, they explained that detaching from tmux lets them reattach later. For `ssh -L 8888:localhost:8888`, they initially typed `localhost:888` and clarified that the missing `8` was a typo. The local endpoint is `http://localhost:8888`, with the local and remote ports both set to 8888. Review complete. Quiz score: 2/3.
