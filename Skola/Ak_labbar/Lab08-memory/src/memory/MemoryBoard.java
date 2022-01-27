package memory;
import java.util.Random;

public class MemoryBoard {
	private int size;
	private String backFileName;
	private String[] frontFileNames;
	private MemoryCardImage[][] board;
	private boolean[][] boolBoard;
	/** Skapar ett memorybräde med size * size kort. backFileName är filnamnet 
	    för filen med baksidesbilden. Vektorn frontFileNames innehåller filnamnen 
	    för frontbilderna. */
	public MemoryBoard(int size, String backFileName, String[] frontFileNames) {
		this.size = size;
		this.backFileName = backFileName;
		this.frontFileNames = frontFileNames;
		this.board = new MemoryCardImage[size][size];
		this.boolBoard = new boolean[size][size];
		createCards(backFileName, frontFileNames);
	}

	/* Skapar size * size / 2 st memorykortbilder.
	   Placerar ut varje kort på två slumpmässiga ställen på spelplanen. */
	private void createCards(String backFileName, String[] frontFileNames) {
		Random rand = new Random();
		int r;
		int c;
		for (int i = 0; i < frontFileNames.length; i++) {
			MemoryCardImage toAdd = new MemoryCardImage(frontFileNames[i], backFileName);
			for (int index = 0; index < 2; index++) {
				do {
					r = rand.nextInt(size);
					c = rand.nextInt(size);
				} while (board[r][c] != null);
				board[r][c] = toAdd;
			}
		}
	}

	/** Tar reda på brädets storlek. */
	public int getSize() {
		return size;
	}
	
	/** Hämtar den tvåsidiga bilden av kortet på rad r, kolonn c.
	    Raderna och kolonnerna numreras från 0 och uppåt. */
	public MemoryCardImage getCard(int r, int c) {
		return board[r][c];
	}

	/** Vänder kortet på rad r, kolonn c. */
	public void turnCard(int r, int c) {
		boolBoard[r][c] = ! boolBoard[r][c];
	}
	
	/** Returnerar true om kortet r, c har framsidan upp. */
	public boolean frontUp(int r, int c) {
		return boolBoard[r][c] ;
	}
	
	/** Returnerar true om det är samma kort på rad r1, kolonn c2 som på rad r2, 
	    kolonn c2. */
	public boolean same(int r1, int c1, int r2, int c2) {
		MemoryCardImage card1 = getCard(r1, c1);
		MemoryCardImage card2 = getCard(r2, c2);
		return card1.equals(card2);
	}

	/** Returnerar true om alla kort har framsidan upp. */
	public boolean hasWon() {
		for (int i = 0; i < boolBoard.length; i++) {
			for (int j = 0; j < boolBoard[i].length; j++) {
				if (!boolBoard[i][j]) {return false;}
			}
		}
		return true;
	}	
}
