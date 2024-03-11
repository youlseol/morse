### 1. Prerequired
- python3 (mac)
- brew install pipx
- brew install ffmpeg

### 1.1 Create virtual environment
```bash
pipx install poetry
```

### 1.2 poetry and toml file references url
https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
https://python-poetry.org/docs/pyproject/


### 2. Run virtual environment
```bash
poetry shell
```

### 3. crewAI installing with packages
```bash
poetry install
```

### 3.1 Add dependancy packages and update
```bash
poetry update
```

### 4. Run
```bash
python3 main.py
```

### 5. Remove virtual environment
```bash
poetry env info --path
rm -rf $(poetry env info --path)
```