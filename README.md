# Grammatical

<img alt="Pink Bubble Tea with cute eyes and smile, using a typewriter, digital art" src="https://user-images.githubusercontent.com/24948340/226350030-912c9696-8bc2-4a70-8f26-966b2814528e.png" width="256">

_Corrects the spelling and grammar of your text using ChatGPT._

# Motivation

I have been using this tool internally for a while now. It excellently simplifies complex technical language and perfectly complements [Grammarly](https://www.grammarly.com/).

# Install

```bash
python3 -m pip install grammatical
```

# Usage

```bash
Usage: grammatical [OPTIONS]

  Corrects the spelling and grammar of the text.

Options:
  --text TEXT               Text input for grammar correction
                            If --text flag is used, a prompt will be displayed to enter the text.
                            By default, the most recent text from the clipboard will be used.

  --api_key TEXT            OpenAI API Key
                            By default, key from the OPENAI_API_KEY env var will be used.

  --tone TEXT               Tone of the grammar correction  [default: "social media"]
                            This can be tuned in based on the context of the text.
                            E.g. "formal/informal setting", "academia", "reddit", etc.

  --simplify                Simplify the text

  -i, --input_format TEXT   Specify the input format  [default: text]
                            Useful when working with files like LaTeX, Markdown.

  -o, --output_format TEXT  Specify the output format  [default: text]
                            Useful when working with files like LaTeX, Markdown.

  --help                    Show this message and exit.
```

## Example

```bash
[09:34][~] # Text in clipboard: I walk to the store and I bought milk
[09:34][~] grammatical
Modified Text:
"I walked to the store and bought milk."
Text copied to clipboard.
[09:34][~]
```

# My MacOS Workflow

For my macOS workflow, I have [created a new `Application` in Automator](https://apple.stackexchange.com/questions/419767/how-to-create-a-shortcut-for-a-command-in-terminal-that-i-can-have-in-my-dock) that runs "Grammatical" for 
convenience. I have also dragged it to the Dock.

Here is the AppleScript that I am using:
```applescript
tell application "Terminal"
    activate
    do script "grammatical"
end tell
```

If you are mostly concerned with the defaults, I highly recommend doing this.

# License

Under [MIT License](https://github.com/pncnmnp/grammatical/blob/master/LICENSE). The logo is [made using Midjourney](https://docs.midjourney.com/docs/terms-of-service) and licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
