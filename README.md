# Usage
## Running the program
```
python main.py [path to engine binary]
```
### Example 
```
python main.py "~/engine.bin"
```
## Commands
| Commands                     | Description                                                                                                                                |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| add random                   | Add a random tile according to the game's rule.                                                                                            |
| add [position] [exponent]    | Add a tile with [exponent] to [position]. Position is ordered 0-16 from left to right and top to bottom starting from the top-left square. |
| position xxxx/xxxx/xxxx/xxxx | Set position, each row is separated by '/' and 'x' representing exponent. e.g. 0002/1110/2322/0000                                         |
| Move [direction]             | Slide the tiles in the given direction. Direction can be 'l', 'r', 'u', or 'd'                                                             |
| go time [millisecond]        | Instruct the engine to search for a specified amount of time.                                                                              |
| show                         | Display the board.                                                                                                                         |
| exit                         | Exit the program.                                                                                                                          |

