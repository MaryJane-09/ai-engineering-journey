# SE 00 Lesson 11: Linux for AI

These notes summarize the [official Linux for AI lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/11-linux-for-ai). The temporary script permissions exercise is complete; see [`experiment.md`](experiment.md).

## Filesystem basics

Linux has one filesystem rooted at `/`. The current user's home directory is `~` (often `/home/<user>`). Use `pwd` to print the current directory, `ls -la` to list visible and hidden files with details, and `cd` to move around. Common tools include `mkdir`, `cp`, `mv`, `cat`, `less`, `grep`, and `find`.

## Permissions and `sudo`

Files have owner, group, and other-user permissions for reading, writing, and executing. If a script you own lacks execute permission, `chmod +x script.sh` adds it. `sudo command` runs one command with administrator privileges, often needed for system package installation with `apt`.

Different permission errors need different fixes. The Lesson 7 Docker error was denied access to `/var/run/docker.sock`; that is daemon access, not a missing execute bit on a script. `chmod +x` would not fix it.

## Disk, processes, and packages

- `df -h` reports free space on mounted filesystems.
- `du -sh <directory>` reports space used by a directory; combine `du`, `sort`, and `head` to find large folders.
- `ps`, `htop`, and `nvidia-smi` help inspect processes and GPU use.
- On Ubuntu, `apt update` refreshes package metadata and `sudo apt install <package>` installs system packages.

## Remote work and platform differences

`scp` copies files over SSH. `rsync` is useful for large or repeated transfers because it sends changed data and can resume interrupted transfers. `tmux` keeps a remote terminal session available to detach and reattach.

macOS and Linux have different `sed -i` syntax: macOS requires an empty string after `-i` (for example, `sed -i '' 's/a/b/' file`); Linux accepts `sed -i 's/a/b/' file`.

## Learner evidence and review

The initial quiz score was 0/3. On a retake with the original questions repeated, the learner answered all three correctly. On a fresh retake, they answered the `rsync` question correctly but missed `~` (home directory) and the `apt update`/`apt install` sequence. The learner then observed a temporary script change from `-rw-rw-r--` to `-rwxrwxr-x` after `chmod +x`, followed by successful execution. In review, the learner identified `~` as the home directory, gave `sudo apt update` followed by `sudo apt install curl`, learned that `du -sh` uses `-s` for a summary and `-h` for human-readable units, and identified the macOS `sed -i ''` syntax. Review complete.
