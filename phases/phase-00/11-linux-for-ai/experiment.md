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
