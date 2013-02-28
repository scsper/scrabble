package driver;

import java.util.ArrayList;

public class Player {
	String name;
	Rack rack;
	Board board;
	TileBag tilebag;
	//boolean turn; //if true, it is the player's turn
//	boolean submit; //if true, the player has submitted the turn
	
	public Player(String n, TileBag t, Board b) {
		name = n;
		tilebag = t;
		board = b;
		rack = new Rack();
	}
	
	public boolean play(String letter, int x, int y) {
		Tile t = new Tile();
		//if board position is empty, return true; if board position is occupied, return false
		if(board.checkBoardPosition(x, y)) {
			//board position == empty
			
			//check if it is on the rack
			if(rack.checkRack(letter)) {
				t = rack.getTile(letter);
				board.fillBoardPosition(t, x, y);
				
				return true;
			} else {
				System.out.println("ERROR P001: Player.java: play(): The tile was not on the rack.");
				return false; //tile was not on the rack
			}
			
		} else {
			System.out.println("ERROR P002: Player.java: play(): The board position was occupied.");
			return false; //board position == occupied
		}
			
			
		//check if it is on the rack
	}
	
	/**
	 * Draws tiles from the tilebag and transfers them to the rack.
	 */
	public void drawTiles() {
		ArrayList<Tile> t = new ArrayList<Tile> ();
		t = tilebag.selectTiles(7 - rack.tiles.size());
		
		rack.fillRack(t);
	}
	
	/**
	 * Receives the illegally played tiles back from the board and places it back on his rack.  
	 * @param t The tiles that are to be taken back
	 */
	public void recoverTiles(ArrayList<Tile> t) {
		rack.fillRack(t);
	}
	
	public String toString() {
		return name + "\n" + rack;
	}
}
