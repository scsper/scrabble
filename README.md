scrabble
========

### Board: singleton
- multi-dimensional list of board positions

##### Interaction API
- place_tile(tile, position)
	- places the tile in the proper board position
	- fires event that triggers "valid_turn" in the game manager
- retrieve_tile(position)
- retrieve_all()


### BoardPosition: helper class
- multiplier, an enum:
	- NONE
	- DOUBLE_WORD
	- DOUBLE_LETTER
	- TRIPLE_WORD
	- TRIPLE_LETTER
- state, an enum:
	- EMPTY
	- PENDING
	- FULL
	- Note: this enum is not necessary...  we can have a is_permanent boolean and use that in conjunction with the Tile being null to accomplish the same thing as this check, but I think this is cleaner.
- Tile

##### Interaction API
- points(): returns the number of points, based on multiplier, state, and tile, for the turn


### Tile:
- letter
- points
- account for blank tiles at some point or another

### TileBag: singleton
- list of tiles

##### Interaction API
- draw(num)
	- end of every turn
- swap(tiles)


### Player
- rack: list of tiles
- points
- name

##### Interaction API
- place(tile, position)
- retrieve(tiles)
- play(turn):
	- swap tiles, move on the board, or pass
	- returns the number of tiles you get back


### Dictionary
- hashmap of words
- perhaps an AI dictionary too, based on the level of AI

##### Interaction API
- is(word)

##### Functions
- read_file(dictionary.txt)


### Game Manager: Singleton -- probably written in javascript
- whose turn is it?
- what is the state of the board? (should these be managed in the board object?)
	- is the board valid?
	- what tiles have been played?

- valid_board(): calculates whether the turn is legal or not
	- triggered after every tile that is placed
- form_word(tiles): makes a word out of the tiles
- Dictionary.is(word)
	- if true:
		- allocate points
			- did the player use the whole rack
			- count in every direction
			- apply multipliers correctly
		- change the board to reflect that the word played is valid
			- update board position state
		- update turns
	- if false:
		- return to the player that he did not make a valid word
			- don't clear the board


### Renderer

##### API
- render_board()
- render_player()
	- points
	- name
	- rack (showing or not)
- render_frame()
- render_tile_bag()


### AI
- reference to the board (python side board model needed)
- rules as to what is a valid word (algorithm should cover this)
- prefix tree of all the words
- understanding of points

##### API
- find_word
	- find all possibilities on the board (DAWG algorithm)
	- keep only the highest scoring word
