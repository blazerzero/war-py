# war-py

Interactive implementation of the [War card game](https://en.wikipedia.org/wiki/War_(card_game)).

## Getting Started

**FIRST:** Make sure you have [pipenv](https://pypi.org/project/pipenv/) installed.

1. Install pip packages
    - `pipenv install`

2. Enter the pip environment
    - `pipenv shell`

3. To play the game:
    - `python war.py`

4. To run the tests:
    - `python war.py test`

---

## Assumptions/Corner Cases

This implementation of War assumes the basic implementation of the game. As most descriptions of War do not explicitly specify what happens if a player runs out of cards during a war, in this implementation, a player automatically loses if they run out of cards during a war.
