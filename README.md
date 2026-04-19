# simple-cmd-program

Simple greeting CLI program made to learn more about CLI's. 

## Setup

```bash
uv sync
source .venv/bin/activate
```

## Usage

```bash
python hello [OPTIONS] [NAME...]
```

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help and exit |
| `-a, --ascii` | Render greeting as ASCII art |
| `-c, --color COLOR` | Colorize the output |

**Examples**

```bash
python hello world
python hello -a world
python hello -c red world
python hello -a -c red world
```
