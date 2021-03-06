# PolyChess By Alpha0

Trello link : https://trello.com/b/2kFbD5MU/notre-projet

Discord server link (for supervision) : https://discord.gg/E3SM5VJ

PolyChess (named polychess as Git repository) is a Chess engine written in Python and modified by Alpha0, a team of students on a course on project management at the engineering school Polytech Annecy-Chambéry. This project is now finished (but not completed !).

The aim of this repository is not to provide any complete Chess engine but the best version we can develop following the client requests in a set limit of time. As a consequence, persons interested in this project should check the different forks of the parent repository.

The required features for PolyChess are:

* PolyChess is able to play against a user, or to play against itself (through UCI and Winboard on Windows, or Arena on Mac)
* The games played are stored in PGN format in a directory games, the PGN headers have to be filled
* PolyChess can render the board either in text (on the console) or in SVG (thanks to python-chess, in Jupyter Notebooks)
* PolyChess has an opening book (first as a Polyglot book, then using your own format)
* PolyChess is able to play on Lichess (and eventually FICS)
* PolyChess is modular, it is then easy to isolate a feature and to modify it
* PolyChess has an AI (easy to modify) that could play for the engine
* It is possible to enter a FEN position and obtain an evaluation from PolyChess

## Milestones for the project

Milestone 1:

PolyChess is able to play against user or another engine through UCI, has an opening book and an AI

Milestone 2:

PolyChess plays on Lichess (and FICS)


# Alpha0 team :

* Robin COLLIAUX  - Chief of Alpha 0
* Rémy MARTIN     - Chief Developer
* Nadia HAMADOU   - Developer
* Beda IGIRANEZA  - Developer

# Features :

* Game saving / loading
* Two gameplays :
  * Player vs AI
  * AI vs AI

# How to start :

To start playing this game, you need first to download python 3 and the python chess library (pip install python-chess).
Then, you can play with our game by executing polychess.py in spider or equivalent.
