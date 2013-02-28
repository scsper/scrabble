package driver;

import java.util.ArrayList;

import driver.BoardPosition.BoardPositionState;

public class BoardScanner {
	Board board;
	int xAnchor, yAnchor; //coordinates for the move that is to be verified
	String direction; //"Across" or "Down" or "Neither" (one letter played) for the direction of the move that is to be verified
	boolean across, down;
	ArrayList<String> words = new ArrayList<String> (); //stores the words played to for checking against the dictionary
	
	public BoardScanner(Board b) {
		board = b;
		xAnchor = -1;
		yAnchor = -1;
		direction = "";
		across = false;
		down = false;
	}
	
	public void printWord() {
		System.out.println("X-Anchor Coordinate: " + xAnchor);
		System.out.println("Y-Anchor Coordinate: " + yAnchor);
		String letter = board.bp.get(yAnchor + (xAnchor * 17)).getLetter();
		System.out.println("Letter at XY Coordinate: " + letter);
	}
	
	/**
	 * Checks the dictionary and verifies that the move is legal (does not go in more than one direction)
	 * If the move is valid, board scanner resets itself for the next move.
	 * @return true if the move is valid, and false if it is not
	 */
	public boolean verifyMove() {
		if(checkDirection() && (checkConnectivity() || board.firstMove) && checkDictionary()) {
			lockTiles();
			across = false;
			down = false;
			direction = "";
			
			if(board.firstMove) {
				board.firstMove = false;
			}
			
			return true;
		} else {
			return false;
		}
	}
	
	public int calculatePoints() {
		return 0;
	}
	
	/**
	 * 
	 * @return If true, then the move is does not go in two directions
	 */
	private boolean checkDirection() {
		for(int i = 0; i < board.bp.size(); i++) {
			//find the anchor point and derive the coordinates
			if(board.bp.get(i).bpState == BoardPositionState.TEMP) {
				xAnchor = i / 17; 						// get the x coordinate
				yAnchor = i % 17; 						// get the y coordinate
				break;
			}
		}
		
		//scan for letters that are not across or down from the anchor point. FAIL (disable x, y coordinate)
		for(int i = 0; i < board.bp.size(); i++) {
			if(board.bp.get(i).bpState == BoardPositionState.TEMP) {
				int x = i / 17;
				int y = i % 17;
				
				if(x != xAnchor && y != yAnchor ) {
					System.out.println("ERROR BS001: BoardScanner.java: checkDirection(): Move is on a diagonal in the anchor plane.");
					return false;
				}
			}
		}
		
		//scan for letters going across, skip over the anchor point. (save with a boolean)
		for(int column = 0; column < 17; column++) {
			if(board.bp.get((17 * xAnchor) + column).bpState == BoardPositionState.TEMP && column != yAnchor) {
				across = true;
			}
		}
		
		//scan for letters going down, skip over the anchor point.  (save with a boolean)
		for(int row = 0; row < 17; row++) {
			if(board.bp.get(yAnchor + (row * 17)).bpState == BoardPositionState.TEMP && row != xAnchor) {
				down = true;
			}
		}
		
		if(across && down) {
			//if both, FAIL
			System.out.println("ERROR BS002: BoardScanner.java: checkDirection(): Move is going both across and down.");
			return false;
		} else if(!across && !down) {
			//if neither, PASS
			direction = "Neither";
			return true;
		} else if (across){
			//check for "jumps"... legal moves cannot have an "empty" board position in between them
			//start at the anchor point
			for(int column = yAnchor + 1; column < 17; column++) {
				if(board.bp.get((17 * xAnchor) + column).bpState == BoardPositionState.EMPTY) {
					if(board.bp.get((17 * xAnchor) + column).bpState != BoardPositionState.EMPTY) {
						System.out.println("ERROR BS003: BoardScanner.java: checkDirection(): Move has a jump going across.");
						return false;
					}
				}
			}
			direction = "Across";
		} else if (down) {
			//check for "jumps"... legal moves cannot have an "empty" board position in between them
			//start at anchor point
			for(int row = xAnchor; row < 17; row++) {
				if(board.bp.get(yAnchor + (row * 17)).bpState == BoardPositionState.EMPTY) {
					if(board.bp.get(yAnchor + (row * 17)).bpState != BoardPositionState.EMPTY) {
						System.out.println("ERROR BS004: BoardScanner.java: checkDirection(): Move has a jump going down.");
						return false;
					}
				}
			}
			direction = "Down";
		} else {
			//do nothing, this case will not be executed
			System.out.println("ERROR BS005: BoardScanner.java: checkDirection(): A non-executable line of code has just been executed.");
			return false;
		}
		return true;
	}
	/**
	 * Verifies that the play is connected to the game in at least one way.
	 * It does this by checking north, south, east, and west of each tile marked "TEMP" starting with the anchor point and direction.  
	 * If any direction has a "FILLED" board position, then it is legally connected.
	 * Else, it is not valid
	 * 
	 * @return 
	 */
	private boolean checkConnectivity() {
		//printWord();
		if(across) {
			for(int column = yAnchor; column < 17; column++) {
				if(board.bp.get((17 * xAnchor) + column).bpState == BoardPositionState.EMPTY) {
					System.out.println("ERROR BS006: BoardScanner.java: checkConnectivity(): The board position was empty.  Hence, the word is not connected.");
					return false;
				} else if(board.bp.get((17 * xAnchor) + column).bpState == BoardPositionState.FILLED) {
					System.out.println("ERROR BS007: BoardScanner.java: checkConnectivity(): The board position was filled.  Hence, the word is connected but the algorithm is not working correctly.");
					return false;
				} else if(board.bp.get((17 * xAnchor) + column).bpState == BoardPositionState.SENTINEL) {
					System.out.println("ERROR BS008: BoardScanner.java: checkConnectivity(): The board position was a sentinel.  Hence, the word is not connected.");
					return false;
				} else { //the board position is a temp
					//look up
					if(board.bp.get((17 * xAnchor) + column - 17).bpState == BoardPositionState.FILLED) {
						return true;
					} 
					//look down
					if(board.bp.get((17 * xAnchor) + column + 17).bpState == BoardPositionState.FILLED) {
						return true;
					}
					
					//look forward
					if(board.bp.get((17 * xAnchor) + column + 1).bpState == BoardPositionState.FILLED) {
						return true;
					} 
					
					//look backward
					if(board.bp.get((17 * xAnchor) + column - 1).bpState == BoardPositionState.FILLED) {
						return true;
					} 
				}
			}
		} else { //direction == down or direction == neither
			//start at anchor point, start going down and checking
			for(int row = xAnchor; row < 17; row++) {
				if(board.bp.get(yAnchor + (row * 17)).bpState == BoardPositionState.EMPTY) {
					System.out.println("ERROR BS009: BoardScanner.java: checkConnectivity(): The board position was empty.  Hence, the word is not connected.");
					return false;
				} else if(board.bp.get(yAnchor + (row * 17)).bpState == BoardPositionState.FILLED) {
					System.out.println("ERROR BS010: BoardScanner.java: checkConnectivity(): The board position was filled.  Hence, the word is connected but the algorithm is not working correctly.");
					return false;
				} else if(board.bp.get(yAnchor + (row * 17)).bpState == BoardPositionState.SENTINEL) {
					System.out.println("ERROR BS011: BoardScanner.java: checkConnectivity(): The board position was a sentinel.  Hence, the word is not connected.");
					return false;
				} else { //the board position is a temp
					//look up
					if(board.bp.get(yAnchor + (row * 17) - 17).bpState == BoardPositionState.FILLED) {
						return true;
					} 
					//look down
					if(board.bp.get(yAnchor + (row * 17) + 17).bpState == BoardPositionState.FILLED) {
						return true;
					}
					
					//look forward
					if(board.bp.get(yAnchor + (row * 17) + 1).bpState == BoardPositionState.FILLED) {
						return true;
					} 
					
					//look backward
					if(board.bp.get(yAnchor + (row * 17) - 1).bpState == BoardPositionState.FILLED) {
						return true;
					} 
				}
			}
		}
		System.out.println("ERROR BS012: BoardScanner.java: checkConnectivity(): This should never happen.  Check connectivity did not find a valid connection nor did it fail for a reason.");
		return false;
	}
	
	/**
	 * Called after legalMove().
	 * @param wordList The words to be checked
	 * @return If all words are in the dictionary, return true.
	 */
	private boolean checkDictionary() {
		wordGenerator();
		
		//check the actual dictionary
		
		return true;
	}
	
	/**
	 * Called within checkDictionary()
	 * Generates words based on the information gathered by checkDirection
	 * Checks the "left" and "right" parts of a word (or "up" and "down" parts)
	 */
	private void wordGenerator() {
		if(across) {
			
		} else {
			
		}
			
	}
	
	/**
	 * If the move is valid, it locks each tile into position on the board
	 */
	private void lockTiles() {
		System.out.println("Tiles were locked");
		for(int i = 0; i < board.bp.size(); i++) {
			board.bp.get(i).lockTile();
		}
	}
}
