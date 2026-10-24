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

## Evidence

**Pending.** Bring back the before/after `ls -l` output and the script's output after the permission change.
