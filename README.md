# Grammatical

<img alt="Pink Bubble Tea with cute eyes and smile, using a typewriter, digital art" src="https://user-images.githubusercontent.com/24948340/226350030-912c9696-8bc2-4a70-8f26-966b2814528e.png" width="256">


_Corrects the spelling and grammar of the text using ChatGPT._

# Motivation

I have been using this as an internal tool for a while now. I use it in conjunction with the free version of Grammarly, which is quite efficient in 
correcting spelling and basic grammar errors. This tool is excellent at simplifying complex technical language.

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

## Example

```bash
[09:34][~] grammatical
Modified Text: 
"I walked to the store and bought milk."
Text copied to clipboard.
[09:34][~]
```

# License

Under MIT License. The logo is [made using Midjourney](https://docs.midjourney.com/docs/terms-of-service) and licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
