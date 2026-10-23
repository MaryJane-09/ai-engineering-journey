# SE 00 Lesson 04: APIs & Keys

These study notes explain the [official APIs & Keys lesson](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/00-setup-and-tooling/04-apis-and-keys). The course content is separated from the learner's recorded progress at the end. Code examples use placeholders only; no API key or live result is included.

## What you should learn

The lesson introduces secure API-key storage, an LLM request through the Anthropic Python SDK, the equivalent raw HTTP request, and common API errors. These ideas matter because later lessons call model providers directly and build agents that make repeated API requests. A key authenticates the request, while the model name and request body specify what the code is asking the service to do.

## The anatomy of an API call

The lesson breaks a call into four parts:

1. **Endpoint:** the URL receiving the request.
2. **API key:** credentials that identify and authorize the account.
3. **Request body:** the model and message or other input.
4. **Response body:** structured data returned by the service.

The basic flow is code → HTTP request with authentication → API server → HTTP response, usually JSON. An SDK wraps this exchange in provider-specific objects and methods; raw HTTP exposes the URL, headers, and JSON directly. The operation is conceptually similar, but each provider has its own endpoint, SDK, and schema.

## Store credentials outside source code

The official lesson demonstrates environment variables in the shell:

```bash
export ANTHROPIC_API_KEY="YOUR_KEY_HERE"
export OPENAI_API_KEY="YOUR_KEY_HERE"
```

`export` places each value in the environment inherited by commands launched from that shell. The lesson also describes putting these assignments in a `.env` file and adding `.env` to `.gitignore`. A key must not be hard-coded in a Python or TypeScript source file because source can be committed and exposed.

Treat `.env` as a local secret file: ignore it, keep real values out of examples and logs, and check `git status` before committing. The official lesson says SDKs read keys from environment variables automatically, but it does not show the code or dependency that loads a `.env` file into a process. A `.env` file is not itself the same thing as an environment variable; this setup detail is a gap in the lesson and should be confirmed before relying on `.env` in a particular runtime.

## Make the SDK request

The course's Python example has this shape:

```python
import os
import anthropic

client = anthropic.Anthropic()
model = os.environ.get("LLM_MODEL", "claude-sonnet-5")

response = client.messages.create(
    model=model,
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}],
)

print(response.content[0].text)
```

`Anthropic()` creates a client that reads the API key from the environment. `LLM_MODEL` lets the caller select a model; if it is unset, the example uses the lesson's default model identifier. `max_tokens` limits the generated output, and `messages` supplies the user input. The SDK returns a structured response object, so the example selects its first content block and prints the text.

The TypeScript example follows the same pattern: instantiate `Anthropic`, choose `process.env.LLM_MODEL` or the lesson default, call `client.messages.create`, and print the first text block. The lesson does not include the SDK installation command in its prose; consult the lesson's own code/project setup rather than guessing a package setup here.

A successful call should print the model's reply, but the exact wording is generated and can vary. The lesson's exercise also notes that the response contains other fields, including usage and stop reason; printing only `.text` hides those details.

## See what the SDK sends: raw HTTP

The official Python example uses the standard library:

```python
import os
import urllib.request
import json

url = "https://api.anthropic.com/v1/messages"
headers = {
    "Content-Type": "application/json",
    "x-api-key": os.environ["ANTHROPIC_API_KEY"],
    "anthropic-version": "2023-06-01",
}
body = json.dumps({
    "model": os.environ.get("LLM_MODEL", "claude-sonnet-5"),
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
}).encode()

request = urllib.request.Request(url, data=body, headers=headers, method="POST")
with urllib.request.urlopen(request) as response:
    result = json.loads(response.read())
    print(result["content"][0]["text"])
```

The endpoint identifies the Messages API. The headers declare JSON, pass the key, and identify the API version. `json.dumps` serializes the Python dictionary and `.encode()` turns it into request bytes. `Request(..., method="POST")` builds the HTTP request. `urlopen` sends it; `json.loads` parses the response bytes back into a Python object. The result is still provider-specific JSON, so its field names must match that API's response schema.

The SDK and raw HTTP versions perform the same kind of request. The SDK makes ordinary application code shorter; raw HTTP is useful for seeing exactly which headers and body are involved when debugging. The lesson's comparison exercise says both response forms contain fields such as `content`, `usage`, and `stop_reason`, represented as dictionary keys in raw JSON and object attributes in the SDK.

## Authentication errors and rate limits

The lesson's wrong-key exercise expects an authentication failure with HTTP **401**. That means the request was not accepted as authenticated; check that the process has the intended key and that it is valid, without printing or sharing the secret.

The lesson defines a **rate limit** as a maximum request rate used to prevent abuse and ensure fair usage. The learner's progress log separately records understanding HTTP **429** as a rate-limit response. The official lesson does not give a retry/backoff procedure or detailed 429 troubleshooting steps, so those should not be inferred from this note.

API calls may incur billing according to the provider and account. The learner's progress log says a live call was deferred because it required separate API billing; this note does not claim a request was made.

## Common mistakes and lesson limits

- **Hard-coding a key:** keep credentials in the environment, not source code.
- **Committing `.env`:** add it to `.gitignore` and inspect status before committing.
- **Assuming `.env` loads automatically:** the lesson does not demonstrate the loader; verify how the chosen runtime makes file values available.
- **Confusing SDK objects with raw JSON:** the access syntax differs even when the response represents the same fields.
- **Sharing full request logs carelessly:** raw headers contain the API key; redact credentials before sharing diagnostics.
- **Assuming all providers share the same schema:** the lesson explicitly says endpoints, SDKs, and request/response schemas vary.

The lesson teaches a first request and a basic 401 check. It does not explain provider-neutral SDK behavior, detailed billing controls, or rate-limit retry policy. Those topics need a later lesson or provider-specific documentation.

## Key takeaways

- An API request needs an endpoint, authentication, input body, and receives a response body.
- Keep API keys outside source control; ignore local secret files.
- SDKs wrap HTTP details; raw HTTP makes endpoint, headers, and JSON visible.
- 401 is an authentication failure; a rate limit caps request frequency, and the learner's log records 429 for that case.

## Self-check

1. What four pieces make up the API call described in the lesson?
2. Why is `export` used before launching a program that needs a key?
3. What details can you inspect directly in the raw HTTP version?
4. Why can a `.env` file exist without its values being available to a process?
5. What does the official lesson say about provider-specific request and response formats?

## Your recorded progress

The progress log records a 3/3 quiz and says the learner explained API key purpose, `.env` loading and ignore rules, the SDK's role, 401 authentication errors, and 429 rate limits. It also records that the troubleshooting artifact was created and a live API call was deferred due to separate billing. The artifact itself is not present in this repository, and no live call is claimed here. See [`LEARNING.md`](../../../LEARNING.md), entry for 2026-10-23, SE 00/04.
