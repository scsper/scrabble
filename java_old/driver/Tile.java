package driver;

/**
 * All tiles should be initialized before the game begins.
 * @author Scott Sperling
 */

public class Tile {
	//Data 
	public String letter;
	public int pointValue;

	public Tile() {
		
	}
	
	/**
	 * @param l The letter of the tile
	 * @param pV The point value of the tile
	 */
	public Tile(String l, int pV) {
		letter = l;
		pointValue = pV;
	}
	
	/**
	 * Overridden function to print the letter and point value of a tile
	 */
	public String toString() {
		return letter + " " + pointValue;
	}
	
}
