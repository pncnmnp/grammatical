import os

import click
import pyperclip
import openai

from rich import print as rprint


def verify_api_key(api_key):
    """
    Verify that the API key is provided.
    """
    if api_key is None:
        raise Exception("Please provide an OpenAI API key")
    else:
        return api_key


def verify_text_length(text):
    """
    Verify that the text is less than 1900 tokens,
    as the output will also require around 1900 tokens.
    From the OpenAI documentation:
    https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
    1 token ~= 4 chars in English
    """
    if len(text) / 4 > 1900:
        paragraphs = text.split("\n\n")
        chunks = list()
        chunks.append(str())
        # Squeeze in as many paragraphs as possible in a single chunk
        for paragraph in paragraphs:
            if len(paragraph) / 4 > 1900:
                raise Exception(
                    "Text is too long. Please keep each paragraph under 1900 tokens or 7600 characters."
                    "If you have a lot of text, please split it into multiple paragraphs."
                    "Each paragraph should be separated by a newline."
                )
            if len(chunks[-1]) / 4 <= 1900:
                chunks[-1] += " \n\n " + paragraph
            else:
                chunks.append(paragraph)
        return chunks
    return [text]


@click.command()
@click.option(
    "--text",
    prompt="Text",
    prompt_required=False,
    help="Text input for grammar correction",
    default=lambda: pyperclip.paste(),
)
@click.option(
    "--api_key", help="OpenAI API Key", default=lambda: os.environ.get("OPENAI_API_KEY")
)
@click.option(
    "--tone",
    help="Tone of the grammar correction",
    default="social media",
    show_default=True,
)
@click.option(
    "--simplify",
    help="Simplify the text",
    default=False,
    show_default=True,
    is_flag=True,
)
@click.option(
    "--input_format",
    "-i",
    help="Specify the input format",
    default="text",
    show_default=True,
)
@click.option(
    "--output_format",
    "-o",
    help="Specify the output format",
    default="text",
    show_default=True,
)
def grammatical(text, api_key, tone, simplify, input_format, output_format):
    """
    Corrects the spelling and grammar of the text.
    """
    openai.api_key = verify_api_key(api_key)
    chunks = verify_text_length(text)
    modified_texts = list()
    for chunk in chunks:
        simplify_text = (
            "Can you also simplify the complex sentences "
            "for better clarity? Keep the meaning intact."
            if simplify
            else ""
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Can you improve the grammar of the following text?"
                    f"And correct the spelling of the words, if necessary?"
                    f"{simplify_text}"
                    f"I need it for {tone}, so keep the tone specific to that."
                    f"The input format of the text is {input_format}"
                    f" and I want the output format to be {output_format}."
                    f"\n\n Text is: {chunk}",
                },
            ],
        )
        resp = response.choices[0]["message"]["content"]
        modified_texts.append(resp)
    rich_print("\n\n".join(modified_texts))


def rich_print(text):
    """
    Print the text in a rich format.
    """
    text = text.strip()
    pyperclip.copy(text)
    rprint(f"[italic red]Modified Text:[/italic red] \n {text}")
    rprint(f"[italic red]Text copied to clipboard.[/italic red]")


if __name__ == "__main__":
    grammatical()
