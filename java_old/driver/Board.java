package driver;

import java.util.ArrayList;

import driver.BoardPosition.BoardPositionState;
import driver.BoardPosition.Multiplier;

public class Board {
	boolean firstMove;

	/** Board, top left is (1, 1) 
	 * 0 - 16 is row 1, 17 - 31 is row 2, etc.
	 */
	public ArrayList<BoardPosition> bp = new ArrayList<BoardPosition> (289);
	
	public Board() {
		firstMove = true; // will be set false after any legal move is played.
		
		//initialize board positions
		for(int i = 0; i < 17; i++) {
			for(int j = 0; j < 17; j++) {
				if(i == 0 || i == 16) {
					bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.SENTINEL));
				} else if(i == 1 || i == 15) {
					if(j == 1 || j == 8 || j == 15) {
						bp.add(new BoardPosition(i, j, Multiplier.TRIPLE_WORD, BoardPositionState.EMPTY));
					} else if (j == 4 || j == 12) {
						bp.add(new BoardPosition(i, j, Multiplier.DOUBLE_LETTER, BoardPositionState.EMPTY));
					} else if (j == 0 || j == 16){
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.SENTINEL));	
					} else {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.EMPTY));
					}
				} else if (i == 2 || i == 14) {
					if(j == 2 || j == 14) {
						bp.add(new BoardPosition(i, j, Multiplier.DOUBLE_WORD, BoardPositionState.EMPTY));
					} else if(j == 6 || j == 10) {
						bp.add(new BoardPosition(i, j, Multiplier.TRIPLE_LETTER, BoardPositionState.EMPTY));
					} else if (j == 0 || j == 16){
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.SENTINEL));	
					} else {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.EMPTY));
					}
				} else if (i == 3 || i == 13) {
					if(j == 3 || j == 13) {
						bp.add(new BoardPosition(i, j, Multiplier.DOUBLE_WORD, BoardPositionState.EMPTY));
					} else if(j == 7 || j == 9) {
						bp.add(new BoardPosition(i, j, Multiplier.DOUBLE_LETTER, BoardPositionState.EMPTY));
					} else if(j == 0 || j == 16) {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.SENTINEL));	
					} else {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.EMPTY));
					}
				} else if (i == 4 || i == 12) {
					if(j == 4 || j == 12) {
						bp.add(new BoardPosition(i, j, Multiplier.DOUBLE_WORD, BoardPositionState.EMPTY));
					} else if(j == 1 || j == 15 || j == 8) {
						bp.add(new BoardPosition(i, j, Multiplier.DOUBLE_LETTER, BoardPositionState.EMPTY));
					} else if(j == 0 || j == 16) {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.SENTINEL));	
					} else {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.EMPTY));
					}
				} else if (i == 5 || i == 11) {
					if(j == 5 || j == 11) {
						bp.add(new BoardPosition(i, j, Multiplier.DOUBLE_WORD, BoardPositionState.EMPTY));
					} else if(j == 0 || j == 16) {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.SENTINEL));	
					} else {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.EMPTY));
					}
				} else if (i == 6 || i == 10) {
					if(j == 2 || j == 6 || j == 10 || j == 14) {
						bp.add(new BoardPosition(i, j, Multiplier.TRIPLE_LETTER, BoardPositionState.EMPTY));
					} else if(j == 0 || j == 16) {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.SENTINEL));	
					} else {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.EMPTY));
					}
				} else if (i == 7 || i == 9) {
					if(j == 3 || j == 13 || j == 7 || j == 9) {
						bp.add(new BoardPosition(i, j, Multiplier.DOUBLE_LETTER, BoardPositionState.EMPTY));
					} else if(j == 0 || j == 16) {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.SENTINEL));	
					} else {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.EMPTY));
					}
				} else { //i == 8
					if(j == 1 || j == 15) {
						bp.add(new BoardPosition(i, j, Multiplier.TRIPLE_WORD, BoardPositionState.EMPTY));
					} else if (j == 4 || j == 12) {
						bp.add(new BoardPosition(i, j, Multiplier.DOUBLE_LETTER, BoardPositionState.EMPTY));
					} else if (j == 8) {
						bp.add(new BoardPosition(i, j, Multiplier.DOUBLE_WORD, BoardPositionState.EMPTY));
					} else if(j == 0 || j == 16) {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.SENTINEL));	
					} else {
						bp.add(new BoardPosition(i, j, Multiplier.NONE, BoardPositionState.EMPTY));
					}
				}
			}
		}
	}
	
	/**
	 * @param x The x-coordinate of the board position
	 * @param y The y-coordinate of the board position
	 * 
	 * @return true if the board position is empty, false if it is full or a sentinel
	 */
	public boolean checkBoardPosition(int x, int y) {
		int index = ((x * 17) - 1); 						// puts it at the end of the row of the x-coordinate
		index -=  17 - y; 									// puts the index at the proper location
		
		if(bp.get(index).bpState == BoardPositionState.EMPTY) {
			return true;
		} else {
			return false;
		}
	}
	
	/**
	 * @param t The tile to be placed on the board
	 * @param x The x-coordinate of the board position
	 * @param y The y-coordinate of the board position
	 * 
	 * @return true if the board position is empty, false if it is full
	 */
	public void fillBoardPosition(Tile t, int x, int y) {
		int index = ((x * 17) - 1); 						// puts it at the end of the row of the x-coordinate
		index -=  17 - y; 									// puts the index at the proper location
		
		bp.get(index).receiveTile(t);
	}
	
	/**
	 * Retrieves all the "temp" tiles from the board and returns them to the player.
	 * @return The tiles that are to be returned to the player
	 */
	public ArrayList<Tile> returnTiles() {
		ArrayList<Tile> t = new ArrayList<Tile> ();
		for(int i = 0; i < bp.size(); i++) {
			Tile temp = bp.get(i).removeTile();
			
			if(temp != null) {
				t.add(temp);
			}
		}
		return t;
	}
	
	/**
	 * Called on every actionPerformed to give real-time updates about points...
	 * This may change to only being called after legalMove
	 *   
	 * Generates a list of all words that the user is attempting to play.
	 * @return A list of words that user is attempting to play
	 */
	/*
	public ArrayList<ScrabbleWord> generateWordList() {
		ArrayList<ScrabbleWord> wordList = new ArrayList<ScrabbleWord>();
		
		return wordList;
	}
*/
	/**
	 * Prints the board.
	 */
	public String toString() {
		String s;
		s = "";
		for(int i = 0; i < bp.size(); i++) {
			
			s += "  " + bp.get(i).toString();
			
			if(((i + 1) % 17) == 0 && i > 15) {
				s += "\n";
			}
			
		}
		return s;
	}
}
