# Setup
Prequisites:
- python3 with pip
- brew (if on macOS, if you're on Linux use your package manager)

1. Install pipenv:
``` shell
pip install pipenv
```

2. Install dependencies:
```
pip install
```

3. Install overmind
```
brew install overmind
```

# Quickstart
Edit `env.example` and use your OpenAI Key.

```
mv env.example .env
```


Start the server:
```
pipenv shell
overmind s
```

Visit http://localhost:8000
