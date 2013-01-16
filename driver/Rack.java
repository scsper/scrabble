package driver;

import java.util.ArrayList;

public class Rack {
	ArrayList<Tile> tiles = new ArrayList<Tile> ();
	
	public Rack() {
		
	}
	
	/**
	 * Tiles are drawn by the player, who then calls fillRack to place his tiles on the rack
	 * @param t The tiles that are drawn by the player
	 */
	public void fillRack(ArrayList<Tile> t) {		
		for(int i = 0; i < t.size(); i++) {
			tiles.add(t.get(i));
		}
	}
	
	/**
	 * Verify the tile is on the rack.
	 * 
	 * @param letter The letter that is to be checked against the rack.
	 * @return If the letter is on the rack, return true, else, return false
	 */
	public boolean checkRack(String letter) {
		for(int i = 0; i < tiles.size(); i++) {
			if(letter.equals(tiles.get(i).letter)) {
				return true;
			}
		}
		
		return false;
	}
	
	/**
	 * Get the tile whose letter is specified in the parameter
	 * 
	 * @param letter The letter of the tile that is to be removed and returned
	 * @return The tile that has the letter on it
	 */
	public Tile getTile(String letter) {
		for(int i = 0; i < tiles.size(); i++) {
			if(letter.equals(tiles.get(i).letter)) {
				return tiles.remove(i);
			}
		}
		
		System.out.println("ERROR R001: Rack.java: getTile(): The tile was not found on the rack.");
		return null;
	}
	
	/**
	 * Prints the letters and point values of the tiles on the rack
	 */
	public String toString() {
		String s = "";
		for(int i = 0; i < tiles.size(); i++) {
			s += tiles.get(i) + " \\ ";	
		}
		return s; 
	}
}
