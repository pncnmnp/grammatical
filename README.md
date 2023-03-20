# grammatical

_Corrects the spelling and grammar of the text using ChatGPT_

# Install

```bash
python3 -m pip install grammatical
```

# Usage

```bash
Usage: grammatical [OPTIONS]

  Corrects the spelling and grammar of the text.

Options:
  --text TEXT     Text input for grammar correction
                  If --text flag is used, a prompt will be displayed to enter the text.
                  By default, the most recent text from the clipboard will be used.

  --api_key TEXT  OpenAI API Key
                  By default, key from the OPENAI_API_KEY env var will be used.

  --tone TEXT     Tone of the grammar correction  [default: "social media"]
                  This can be tuned in based on the context of the text.
                  E.g. "formal/informal setting", "academia", "reddit", etc.

  --simplify      Simplify the text

  --help          Show this message and exit.
```

# License

Under MIT License
