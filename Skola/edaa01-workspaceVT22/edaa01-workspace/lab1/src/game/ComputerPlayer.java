package game;

import java.util.Random;

public class ComputerPlayer extends Player{
	
	public ComputerPlayer(String userId) {
		super(userId);
	}
	
	public int takePins(Board board) {
		Random rand = new Random();
		int choice = rand.nextInt(Math.min(2, board.getNoPins())) + 1;
		board.takePins(choice);
		return choice;
	}
}
