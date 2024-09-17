# ASC - LLM Chat from the command-line

A command-line tool for interacting with LLMs.

# Why should you use this?

- If you're a command-line junkie, no need to switch to another tool
- Use pay-as-you-go pricing for LLM providers (API vs. Chat)

# Features

- Multi-provider support
  - Ollama
  - OpenAI
  - Anthropic
- Streaming responses
- Persistent command-line history
- Chat history & reset (start new chat)
- Switch provider and model
- Markdown output

# Possible future features

- Support for more LLM providers
- Support RTL languages
- Save output to file
- Patterns library
- Upload files
- Support more modes (image generation, transcription, etc.)
- Automated testing?

# Installation

    clone the repository
    install dependencies: `pip install -r requirements.txt`
    install the package: `pip install .`

    Later, when the package will be available on PyPI, you will be able to install it via pip:
    `pip install azc`

# Running

    ```bash
    % azc
    > how tall is the eifel tower?
    openai:gpt-4o-mini: The Eiffel Tower is approximately 1,083 feet (330 meters) tall, including its antennas. The structure itself, without antennas, is about 1,063 feet (324 meters).
    > q
    Bye!
    %

    You can specify the first prompt as a command-line argument:

    % azc "what is the capital of the moon?"
    gpt-4o-mini: The capital of the moon is called "New Moon".
    >
    ```

# Commands

- `q` or `exit` - exit the program
- `h` or `?` - show help
- `l` - list models
- `n` - start new chat
- `p` - Change provider
- `m` - Change model

# Setup

You will need to configure at least one LLM API.

For example, if using the OpenAPI Completion API, you should create a .env file which contains your API Key.

See `.env.sample` for a sample file

Here are the links to the API sign-up pages (or download in case of Ollama):

- [OpenAI](https://platform.openai.com/signup)
- [Anthropic](https://console.anthropic.com/register)
- [Ollama](https://ollama.com/)

# Contributing

Contributions are welcome! Please feel free to submit a PR.

# License

MIT
