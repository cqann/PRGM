package game;

import javax.swing.JOptionPane;

public class HumanPlayer extends Player {
	
	public HumanPlayer(String userId) {
		super(userId);
	}
	
	public int takePins(Board board) {		
		String choiceStr = JOptionPane.showInputDialog(null, "Choose to remove one or two sticks");
		if (choiceStr == null) {return -2;}
		int choice = parseChoice(choiceStr);
		while (choice > 2 || choice < 1 || choice > board.getNoPins()) {
			choiceStr = JOptionPane.showInputDialog(null, "Invalid choice, choose again");
			if (choiceStr == null) {return -2;}
			choice = parseChoice(choiceStr);
		}
		
		board.takePins(choice);
		return choice;
	}
	
	private int parseChoice(String choiceStr) {
		int toReturn = 0;
		try {
	        toReturn = Integer.parseInt(choiceStr);
	    } catch (NumberFormatException nfe) {
	        toReturn = -1;
	    }
		return toReturn;
	}

}
