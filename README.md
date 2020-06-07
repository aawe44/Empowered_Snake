# Empowered Snake: An extension of the classic Snake game

This "Empowered Snake" game is the power enhanced version of the classic Snake game, with extra features and extra fun. Empowered Snake characterizes:

1. two snakes playing together in one window, Adding more challenge and more competitiveness.

2. inevitable reward from food, allowing snakes crossing itself during a short period

Author: Jason Chen (CONTACT INFORMATION)

Skype ID: 

Email: 







# Game illustration / Demo


|![Screen 1](https://raw.githubusercontent.com/aawe44/pic_for_OOD_snake/master/gif/two.gif)|![Screen 2](https://raw.githubusercontent.com/aawe44/pic_for_OOD_snake/master/gif/single.gif)
|---------------------------------------------|---------------------------------------------|
|Two players competing each other by each controlling a snake on the board|Self-crossing in the inevitable mode



# Installation

There are instant-play mode and Pygame-compile mode. 

1. instant-play: run the exe/dmg/xxx file from release.

2. pygame-compile:

`pip install pygame`

`cd Empowered_Snake`

`python empowered_snake.py`



# Developer Notes

1. The framework is developed in PyGame, utilizing interactive game window, keyboard/mouse control, and gameplay time-series features, etc..
2. The development is based on Object-Oriented Programming, in which XXX (介绍一下不同的文件代表不同的类, 以及不同的类之间的关系)
3. Inevitable Reward functionality:
3.1. Add random seed to the food generated, making some of them in different color XXX
3.2. Whenever the snake eats the food, start a time counter and turn the game-loop into XXX mode.
3.3. in the XXX mode, modify the collision function so that XXX
3.4. When counter ends...
4. Two-Snake functionality: 
4.1 XXX


8. we use XXX module to export the game to executable files for different OS systems, see `XXX.py` for details.



# Controls
## Single player       

| Action       | Button - Single player |
|--------------|------------------------|
| Move Left    | <kbd>Left</kbd>        |
| Move right   | <kbd>Right</kbd>       |
| Move up      | <kbd>Up</kbd>          |
| Move down    | <kbd>Down</kbd>        |


## Two players (Player 1 and Player 2)

| Action       | Button - Player 1   | Button - Player 2 |
|--------------|---------------------|--------------|
| Move Left    | <kbd>Left</kbd>     |<kbd>A</kbd>     |
| Move right   | <kbd>Right</kbd>    |<kbd>F</kbd>     |
| Move up      | <kbd>Up</kbd>       |<kbd>W</kbd>     |
| Move down    | <kbd>Down</kbd>     |<kbd>S</kbd>     |


