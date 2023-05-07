
# COMPUTOR V1

## Table of Contents

- [About](#about)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

    A small python app that solves up to 2nd degree polynomial equations.

### Prerequisites

    python3 or docker compose v2

## Usage <a name = "usage"></a>

The equation must be in the format:

"a\*x^2 + b\*x^1 + c\*x^0 = 0\*x^0"

Any variation and additional segments are allowed, as long as they respect the format.
For example: a\*x^2 + b\*x^2 = c\*x^0 - d\*x^1 is valid.

```
cd app
python3 computor.py <the equation to solve>
```

or

```
docker-compose run -e EQ=<the equation to solve> computor_container bash -c 'python3 computor.py "$EQ"'
```
