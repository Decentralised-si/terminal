# DSI Agent Terminal

An AI agent for your terminal, connected to the [Decentralised.si](https://decentralised.si) network with one API key. It reads and edits files, runs commands, browses, remembers, and uses skills — and every model call goes through **DSI Axon**, the network's blind router, which picks the model for each conversation (`auto`) or uses the one you choose.

Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) by Nous Research (MIT licence).

## Install

**macOS, Linux, WSL, Android (Termux):**

```bash
curl -fsSL https://decentralised.si/install/agent.sh | bash
```

**Windows (PowerShell):**

```powershell
iex (irm https://decentralised.si/install/agent.ps1)
```

The installer sets up Python, the agent and a `dsi-agent` command, then asks for your API key. Create one in the [console](https://decentralised.si/app#/console/keys). To install without the prompt, pass it in:

```bash
DSI_API_KEY=ds_live_... curl -fsSL https://decentralised.si/install/agent.sh | bash
```

## Use

```bash
dsi-agent                                  # interactive session
dsi-agent -z "summarise README.md"         # one question, answer only
dsi-agent -m auto                          # let the router choose (default)
dsi-agent config set DSI_API_KEY ds_live_...   # set or change your key
dsi-agent setup                            # other providers, messaging, tools
dsi-agent update                           # update to the latest version
```

The `hermes` command is installed too and does the same thing.

## How it connects

The agent talks to the network's OpenAI-compatible API:

| Setting | Value |
|---|---|
| Provider | `decentralised` (aliases `dsi`, `decentralised-si`) |
| Base URL | `https://api.decentralised.si/openai/v1` |
| Key | `DSI_API_KEY` (a `ds_` key), stored in `~/.hermes/.env` |
| Model | `auto`, or any model your account can reach (`/models`) |

Your account decides what `auto` can use: open models on the network, hosted open models, and commercial models through your own vendor keys (Console → Providers). Usage and spend show up in the console like any other API call.

## Credits and licence

DSI Agent Terminal is a rebranded build of Hermes Agent by Nous Research, released under the MIT licence (see `LICENSE`). The original README is in [`README.hermes.md`](README.hermes.md).
