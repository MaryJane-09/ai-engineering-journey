# SE 00 Lesson 11: Script Execute Permission

## Goal

Observe how the execute permission changes whether a shell script can run.

## Procedure

Run these commands in your shell:

```bash
check_dir="$(mktemp -d)"
printf '#!/bin/sh\necho permissions-ok\n' > "$check_dir/check.sh"
ls -l "$check_dir/check.sh"
"$check_dir/check.sh"
chmod +x "$check_dir/check.sh"
ls -l "$check_dir/check.sh"
"$check_dir/check.sh"
```

The first run should be denied because the file lacks execute permission. `chmod +x` adds that permission to the temporary script; the second run should work.

## Observed result

Before `chmod +x`, `ls -l` showed `-rw-rw-r--`; executing the script returned `permission denied`. After `chmod +x`, `ls -l` showed `-rwxrwxr-x`, and the script printed `permissions-ok`.

**Status: Complete.** Adding the execute bit allowed the script to run.

## Build practice

### Question 11 — Write a disk-usage report script

Create `storage-report.sh` that accepts one or more file or directory paths as command-line arguments and prints each path's size using `du -sh`. If no paths are given, print a short usage message and exit with a nonzero status. Make the script executable with `chmod +x`, then run it on `phases/phase-00/11-linux-for-ai` and `phases/phase-00/11-linux-for-ai/notes.md`. Record the script, commands, output, and what `-s` and `-h` mean in `du -sh`.

**Answer and evidence:** The learner wrote this script:

```bash
#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <path1> [path2] [path3] ..." >&2
    exit 1
fi

for path in "$@"; do
    if [ -e "$path" ]; then
        du -sh "$path"
    else
        echo "Error: '$path' does not exist." >&2
    fi
done
```

After making it executable, the learner ran:

```bash
./phases/phase-00/11-linux-for-ai/storage-report.sh \
  phases/phase-00/11-linux-for-ai \
  phases/phase-00/11-linux-for-ai/notes.md
```

Output:

```text
20K     phases/phase-00/11-linux-for-ai
4.0K    phases/phase-00/11-linux-for-ai/notes.md
```

Running the script with no arguments printed its usage message and exited with a nonzero status. The learner explained that `-s` prints one summary per path and `-h` formats sizes in human-readable units.
