# SE 00 Lesson 04: Experiment

## Recorded evidence

The learner scored **3/3**, created a troubleshooting artifact according to the progress log, and deferred a live API request because it would require separate billing. The artifact itself is not in this repository, and no live API call is claimed.

## Safe practice experiment

Without using a real credential or making a network request, create a local `.env.example` containing a clearly fake placeholder such as `API_KEY=replace-me`. Check that real `.env` files are ignored by Git before ever placing a credential in one. Record the exact `git check-ignore` command and result; do not put a real key in the example or terminal transcript.

## Practice exercise

### Question 4 — Check API key configuration

Write `api_verification.py` to check whether `API_KEY` is available to the program. Print a clear configured/missing status without printing the key. Run it once with the variable available and once without it, and record both outputs. Do not make a network request.

**Answer and evidence:** The learner's script uses `load_dotenv()` to load local environment settings, then `os.getenv("API_KEY")` to check the value. It prints a boolean and a status message, without revealing the value:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_status = os.getenv("API_KEY")

if api_status:
    print(True)
    print("API key configured")
else:
    print(False)
    print("API key missing")
```

With the key available:

```text
True
API key configured
```

With the key unavailable:

```text
False
API key missing
```

The check distinguishes a configured value from a missing value without printing the value itself. No network request was made.

## Status

Quiz evidence, the billing-related deferral, and the API key status exercise are recorded. The local `.env` file is excluded by the repository ignore rules.
