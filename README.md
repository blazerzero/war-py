# war-py

Interactive implementation of the [War card game](https://en.wikipedia.org/wiki/War_(card_game)).

## Getting Started

**FIRST:** Make sure you have [pipenv](https://pypi.org/project/pipenv/) installed.

1. Install pip packages
    - `pipenv install`

2. To play the game:
    - `pipenv run python war.py`

3. To run the tests:
    - `pipenv run python war.py test`

---

## Assumptions/Corner Cases

This implementation of War assumes the basic implementation of the game. As most descriptions of War do not explicitly specify what happens if a player runs out of cards during a war, in this implementation, a player automatically loses if they run out of cards during a war.

## Next Steps

If I had more time, I would write more tests on the different pieces of the play function itself, such as making sure that the card-comparing cases are defined correctly and that the functionality for entering war is correct as well.
