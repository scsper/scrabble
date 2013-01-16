package driver;

import java.util.ArrayList;

public class TileBag {
	ArrayList<Tile> tiles = new ArrayList<Tile> ();
	
	/**
	 * Initialize the tiles and scramble them.
	 * To be called before the game starts.
	 */
	public TileBag() {
		for(int i = 0; i < 12; i++) {
			tiles.add(new Tile("e", 1));
		}
		
		for(int i = 0; i < 9; i++) {
			tiles.add(new Tile("a", 1));
			tiles.add(new Tile("i", 1));
		}
		
		for(int i = 0; i < 8; i++) {
			tiles.add(new Tile("o", 1));
		}
		
		for(int i = 0; i < 6; i++) {
			tiles.add(new Tile("n", 1));
			tiles.add(new Tile("r", 1));
			tiles.add(new Tile("t", 1));
		}
		
		for(int i = 0; i < 4; i++) {
			tiles.add(new Tile("l", 1));
			tiles.add(new Tile("s", 1));
			tiles.add(new Tile("u", 1));
			tiles.add(new Tile("d", 2));
		}
		
		for(int i = 0; i < 3; i++) {
			tiles.add(new Tile("g", 2));
		}
		
		for(int i = 0; i < 2; i++) {
			tiles.add(new Tile("blank", 0));
			tiles.add(new Tile("b", 3));
			tiles.add(new Tile("c", 3));
			tiles.add(new Tile("m", 3));
			tiles.add(new Tile("p", 3));
			tiles.add(new Tile("y", 4));
			tiles.add(new Tile("f", 4));
			tiles.add(new Tile("h", 4));
			tiles.add(new Tile("w", 4));
			tiles.add(new Tile("v", 4));
		}
		
		tiles.add(new Tile("k", 5));
		
		tiles.add(new Tile("j", 8));
		tiles.add(new Tile("x", 8));
		
		tiles.add(new Tile("q", 10));
		tiles.add(new Tile("z", 10));
		
		scrambleTiles();
	}

	/**
	 * Take the tiles that a user has traded in, put them back in the back, and scramble the order
	 * @param t The tiles that are to be put back in the bag
	 */
	public void reinsertTiles(ArrayList<Tile> t) {
		int size = t.size();
		for(int i = 0; i < size; i++) {
			tiles.add(t.remove(i));
		}
		
		scrambleTiles();
	}
	
	/**
	 * Give the user the number of tiles that he requests.
	 * Should be called at the end of every turn.
	 * @param numOfTiles The number of tiles requested
	 * @return The tiles selected from the bag or null if there are no more tiles in the bag
	 */
	public ArrayList<Tile> selectTiles(int numOfTiles) {
		ArrayList<Tile> t = new ArrayList<Tile> ();
		
		for(int i = 0; i < numOfTiles; i++) {
			if(tiles.size() == 0) { // if the tilebag is empty 
				if(t.size() == 0) {
					return null; 	// if there are no tiles in the bag, return null
				} else {
					return t; 		// if the bag ran out of tiles, send back the drawn tiles 
				}
			} else {
				t.add(tiles.remove(0)); // pop the first tile off of the tiles array
			}
		}
		return t; 						// return the number of tiles requested by the player
	}
	
	/**
	 * 
	 * @return The number of tiles left in the bag
	 */
	public int getTilesLeft() {
		return tiles.size();
	}
	
	
	/**
	 * Randomizes the order of the tiles. 
	 */
	private void scrambleTiles() {
		ArrayList<Tile> tempTiles = new ArrayList<Tile> ();
		long rand;
		int size = tiles.size();
		
		for(int i = 0; i < size; i++) {
			rand = Math.round(Math.random() * 10000);
			rand = rand % tiles.size();
			
			tempTiles.add(tiles.remove((int)rand));
		}
		
		tiles = tempTiles;
	}
	
	/**
	 * Prints the tile bag.
	 */
	public String toString() {
		String s = "";
		for(int i = 0; i < tiles.size(); i++) {
			s += tiles.get(i) + "\n";
		}
		
		return s;
	}

}
