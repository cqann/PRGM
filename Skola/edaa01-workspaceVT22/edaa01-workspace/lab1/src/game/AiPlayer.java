package game;

public class AiPlayer extends Player{
	public AiPlayer(String userId) {
		super(userId);
	}
	
	public int takePins(Board board) {
		int noPins = board.getNoPins();
		int choice = noPins % 3;
		choice = choice == 0 ? 1 : choice;
		board.takePins(choice);
		return choice;
	}
}
