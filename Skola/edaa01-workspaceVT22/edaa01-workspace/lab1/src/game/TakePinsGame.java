package game;

import javax.swing.JOptionPane;

public class TakePinsGame {
	
	public static void main(String[] args) {
		Board board = new Board();
		HumanPlayer human = new HumanPlayer("You");
		AiPlayer computer = new AiPlayer("Ai");
		Player player = null;
		board.setUp(21);
		int i = 1;
		int choice = 0;
		while(board.getNoPins() > 0) {
			JOptionPane.showMessageDialog(null, board.getNoPins() + " left...");
			player = i % 2 == 0 ? human : computer;
			
			choice = player.takePins(board);
			if (choice == -2) {
				break;
			}
			JOptionPane.showMessageDialog(null, player.getUserId() + " took " + choice + " pins!" );
			i++;
		}
		if (choice != -2) {
			JOptionPane.showMessageDialog(null, player.getUserId() + " won!");
		}
	}
}
 	 