# ConnectForks

The objective of this program is to encode a game of Connect Four where the user can adjust the size of the game.

## Limitations 

There are a few limitations to this program. For one, the code is strictly limited to vertical and horizontal eliminations, and therefore cannot detect a victory if the positions are lined up diagonally. Beyond that, the runtime on this code is O(n) to O(n<sup>2</sup>) complexity which means that the program may take exponentially long to process as the game board expands.

## Future Improvements

Moving forward with this code, I plan on implementing a hashmap to fine tune the time complexity of the program. I also plan on implementing a diagonal search in my program so victories can be won diagonally. Finally, in the far future, I would like to be able to program a bot that would be able to play in case if there is only one player.
