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
python hello world
python hello -a world
python hello -c red world
python hello -a -c red world
```
