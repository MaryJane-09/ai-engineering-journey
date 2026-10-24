# SE 00 Lesson 11: Reflection

## Learner reflection

The learner initially missed all three quiz questions, then answered the repeated questions correctly. In a fresh retake, they identified `rsync`'s use for large transfers but missed the meaning of `~` and the Ubuntu package installation sequence. In the hands-on exercise, they saw execution denied before `chmod +x` and `permissions-ok` afterward.

## Takeaway

`chmod +x` fixes a missing execute bit on a script. The learner observed the mode change from `-rw-rw-r--` to `-rwxrwxr-x`. This does not fix unrelated permission problems such as access to Docker's daemon socket.

## Question to revisit

What does `~` stand for, and which two commands refresh Ubuntu's package list and install a package?
