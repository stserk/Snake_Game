# Snake Game

This is a classic Snake Game implemented in Python using the Turtle graphics library. The game involves controlling a snake to eat food and grow in size, while avoiding collisions with walls and its own tail.

## Features

- Classic snake gameplay
- Increasing difficulty as the snake grows
- Score tracking
- Simple and intuitive controls

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game.

2. **Control the Snake**:
    - Use the **Up arrow key** to move up.
    - Use the **Down arrow key** to move down.
    - Use the **Left arrow key** to move left.
    - Use the **Right arrow key** to move right.

3. **Objective**: Guide the snake to eat the food that appears on the screen. Each time the snake eats food, it grows in length.

4. **Avoid Collisions**:
    - Do not let the snake hit the walls.
    - Do not let the snake collide with its own tail.

5. **Game Over**: The game ends if the snake hits the wall or its own tail.

## Project Structure

- `main.py`: The main script to run the game.
- `food.py`: Contains the `Food` class, responsible for placing food on the screen.
- `snake.py`: Contains the `Snake` class, which manages the snake's movement and growth.
- `scoreboard.py`: Contains the `Scoreboard` class, which displays the current score.
- `food.gif`, `snake.gif`: Graphic assets used in the game.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Install Dependencies**:
    - Ensure you have Python installed (Python 3.6 or higher recommended).
    - Install the Turtle graphics library if not already installed:
      ```bash
      pip install PythonTurtle
      ```

3. **Run the Game**:
    ```bash
    python main.py
    ```

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are reviewed on a regular basis.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgements

- [Turtle Graphics](https://docs.python.org/3/library/turtle.html) for the graphics library.
- Inspiration from classic Snake games.
