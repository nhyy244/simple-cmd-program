# Greeting CLI program

Simple greeting CLI program made to learn more about CLI's. 

## Setup
Install with pip/pipx:
```bash
pip install hello24
pipx install hello24
```

## Usage

```bash
hello [OPTIONS] [NAME...]
```

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help and exit |
| `-a, --ascii` | Render greeting as ASCII art |
| `-c, --color COLOR` | Colorize the output |

**Examples**

```bash
hello world
hello -a world
hello -c red world
hello -a -c red world
```
