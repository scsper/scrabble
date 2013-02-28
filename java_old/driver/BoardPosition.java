package driver;

public class BoardPosition {
	/** Data **/
	public int x, y; //coordinates: (0, 0) is top left
	private Tile tile;
	private String output; //temporary string for display purposes
	
	/** Multiplier Enum
	 * 
	 * Stands for each of the bonuses that exist in Scrabble.
	 */
	public enum Multiplier { NONE, DOUBLE_LETTER, DOUBLE_WORD, TRIPLE_LETTER, TRIPLE_WORD };
	public Multiplier multiplier;
	
	/** Board Position State Enum
	 * 
	 * EMPTY = no tile (default)
	 * TEMP = player has placed a tile but has not submitted his/her turn
	 * FILLED = tile has been submitted
	 */
	public enum BoardPositionState { EMPTY, SENTINEL, TEMP, FILLED };
	public BoardPositionState bpState;
	
	/**
	 * No board position will be filled before the game is started.
	 * @param x x-coordinate (rows)
	 * @param y y-coordinate (columns)
	 */
	public BoardPosition(int x, int y, Multiplier m, BoardPositionState b) {
		bpState = b;
		multiplier = m;
		this.x = x;
		this.y = y;
		
		if(multiplier.equals(Multiplier.NONE)) {
			output = "-";
		} else if (multiplier.equals(Multiplier.DOUBLE_LETTER)) {
			output = "2";
		} else if (multiplier.equals(Multiplier.TRIPLE_LETTER)) {
			output = "3";
		} else if (multiplier.equals(Multiplier.DOUBLE_WORD)) {
			output = "4";
		} else { //triple word
			output = "5";
		}
		
		if(bpState.equals(BoardPositionState.SENTINEL)) {
			output = "~";
		}
	}
	
	/**
	 * Receives a tile and makes it temporary if the tile is empty.  
	 * @param t The tile to be placed in the board position
	 * @return If making the tile temporary was successful, return true; else, the tile was occupied, return false
	 */
	public boolean receiveTile(Tile t) {
		if(bpState.equals(BoardPositionState.EMPTY)) {
			tile = t;
			bpState = BoardPositionState.TEMP; //board position is temporarily filled
			output = tile.letter;
			return true;
		} else {
			return false;
		}
	}
	
	/**
	 * Removes a recalled temporary tile from the board.
	 * This can be specified by the user or automatically done by the game on an illegal move
	 * @return Tile that is to be returned
	 */
	public Tile removeTile() {
		if(bpState.equals(BoardPositionState.TEMP)) {
			Tile temp;
			temp = tile;
			tile = null;
			bpState = BoardPositionState.EMPTY;
			
			if(multiplier.equals(Multiplier.NONE)) {
				output = "-";
			} else if (multiplier.equals(Multiplier.DOUBLE_LETTER)) {
				output = "2";
			} else if (multiplier.equals(Multiplier.TRIPLE_LETTER)) {
				output = "3";
			} else if (multiplier.equals(Multiplier.DOUBLE_WORD)) {
				output = "4";
			} else { //triple word
				output = "5";
			}
			
			return temp;
		} else {
			return null;
		}
	}
	
	/**
	 * Locks a temporary tile in place when a move is validated.
	 */
	public void lockTile() {
		if(bpState.equals(BoardPositionState.TEMP)) {
			bpState = BoardPositionState.FILLED;
		}
	}
	
	public String getLetter() {
		return tile.letter;
	}
	
	public String toString() {
		return output;
	}
}
