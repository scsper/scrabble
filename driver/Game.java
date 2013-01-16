package driver;

import java.util.Scanner;

public class Game {
	Board board;
	BoardScanner boardScanner;
	TileBag tilebag;
	Player human;
	Player ai;
	boolean playerTurn;
	boolean game;
	Scanner s = new Scanner(System.in);
	
	public Game() {
		board = new Board();
		boardScanner = new BoardScanner(board);
		tilebag = new TileBag();
		human = new Player("Scott", tilebag, board);
		ai = new Player("AI", tilebag, board);
		playerTurn = true;
		game = true;
		
		print();
		human.drawTiles();
		ai.drawTiles();
	}
	
	/**
	 * Contains the main gameplay mechanics; controls whose turn it is
	 */
	public void play() {
		while(game) {
			if(playerTurn) {
				System.out.println("Human Play Letter");
				if(playLetter()) {
					//go through steps of verification
					print();
				} else {
					//
				}
			} else {
				System.out.println("AI Play Letter");
				if(AIplayLetter()) {
					//go through steps of verification
					print();
				} else {
					//
				}
			}
		}
	}
	
	/**
	 * Prints the board, the number of tiles left in the tilebag, and the racks of the two players.
	 */
	public void print() {
		System.out.println(board);
		System.out.println("Tiles Left: " + tilebag.tiles.size());
		System.out.println("\n" + human);
		System.out.println("\n" + ai);
		System.out.println("-------------------------------------------------\n");
	}
	
	public boolean playLetter() {
		System.out.println("Enter the letter you wish to play and the coordinates you wish to play at.  If you would like to end your turn, press 1.");
		String letter = s.next();
		if (!letter.equals("1")) {
			int x = s.nextInt();
			int y = s.nextInt();
			
			return human.play(letter, x, y);
		} else {
			submitted();
			//there should be nothing afterwards
			return true;
		}
	}
	
	public boolean AIplayLetter() {
		System.out.println("Enter the letter you wish to play and the coordinates you wish to play at.  If you would like to end your turn, press 1.");
		String letter = s.next();
		if (!letter.equals("1")) {
			int x = s.nextInt();
			int y = s.nextInt();
			
			return ai.play(letter, x, y);
		} else {
			submitted();
			//there should be nothing afterwards
			return true;
		}
	}

	private void submitted() {
		//go through verification
		if(boardScanner.verifyMove()) {
			if(playerTurn) {
				human.drawTiles();
				//add points
			} else {
				ai.drawTiles();
				//add points
			}
			playerTurn = !playerTurn; 		// toggle playerTurn
		} else {
			if(playerTurn) {
				human.recoverTiles(board.returnTiles());
			} else {
				ai.recoverTiles(board.returnTiles());
			}
		}
	}
	
	public static void main(String[] args) {
		Game scrabble = new Game();
		
		scrabble.print();
		scrabble.play();
	}
}
