package memory;

public class MemoryGame {
	public static void main(String[] args) {
		String[] frontFileNames = {"can.jpg", "flopsy_mopsy_cottontail.jpg",
				"friends.jpg", "mother_ladybird.jpg", "mr_mcgregor.jpg",
				"mrs_rabbit.jpg", "mrs_tittlemouse.jpg", "radishes.jpg" };
		
		MemoryBoard gameBoard = new MemoryBoard(4, "back.jpg", frontFileNames);
		
		MemoryWindow w = new MemoryWindow(gameBoard);
		w.drawBoard();
		int r1, c1, r2, c2;
		int nTries = 0;
		boolean[][] locked = new boolean[4][4];
		while (!gameBoard.hasWon()){
			w.waitForMouseClick();
			r1 = w.getMouseRow();
			c1 = w.getMouseCol();
			if (locked[r1][c1]){continue;}
			gameBoard.turnCard(r1, c1);
			w.drawCard(r1, c1);
			do {
				w.waitForMouseClick();
				r2 = w.getMouseRow();
				c2 = w.getMouseCol();
			} while ((r1 == r2 && c1 == c2) || locked[r2][c2] );
			
			gameBoard.turnCard(r2, c2);
			w.drawCard(r2, c2);
			MemoryWindow.delay(700);
			
			if (!gameBoard.same(r1, c1, r2, c2)){
				gameBoard.turnCard(r1, c1);
				gameBoard.turnCard(r2, c2);
				w.drawBoard();
			} else {
				locked[r1][c1] = true;
				locked[r2][c2] = true;
			}
			nTries += 1;
		}
		w.getAdvancedControls().setFontSize(60);
		w.moveTo(w.getWidth()/2-300, w.getHeight()/2-20);
		w.writeText("DU VANN, med " + nTries + " försök");

	}
}
