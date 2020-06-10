# Empowered Snake: An extension of the classic Snake game

This "Empowered Snake" game is the power enhanced version of the classic Snake game, with extra features and extra fun. Empowered Snake characterizes:

1. two snakes playing together in one window, Adding more challenge and more competitiveness.

2. inevitable reward from food, allowing snakes crossing itself during a short period

Author: Jason Chen (CONTACT INFORMATION)

Skype ID: jasonmrchen

Email: aawe44@gmail.com







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

1. The framework is developed in PyGame, utilizing interactive game window, keyboard/mouse control, and game play time-series features, etc..

2. The development is based on Object-Oriented Programming, in which game_class folder
    * game_state.py: 
        * show game start/over         
    * snake.py: Display snake body.
         * Attributes: location, length, color...etc. 
         * Behavior: move, grow, display               
    * food.py: 
        * Randomly generated food         
    * scoreboard.py: 
        * Record the score: players get one point for each food.           
    

3. Main program empowered_snake.py
     * After the game starts, the start screen is displayed by game_state.py.   
     * After entering the game, three objects are generated, snake, food, scoreboard.    
     * Receive keyboard commands to control the moving direction of the snake.    
     * After moving, there are three possible states        
        1. When the snake touches itself, end the game.    
        2. When the snake touches the food, the snake grows itself. Create new food, update scoreboard   
        3. When the snake touches the open ground, continue the game
    
3. Inevitable Reward functionality:
    * Add random seed to the food generated, making some of them in black color.
    * Whenever the snake eats the food, start a time counter and turn the game-loop into inevitable mode.
    * In the inevitable mode, modify the collision function so that snake can self-cross.
    * When counter ends snake return to normal mode.

4. Two-Snake functionality: 
    * Can be played by two players at the same time
    * The player loses the game, 
        * When the player's snake self-cross
        * When the player's snake touches another player's snake 
    
5. we use pyinstall module to export the game to executable files for different OS systems, see `XXX.py` or `export.py` for details.



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


