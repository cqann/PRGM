package game;

public class Board {
	private int noPins;
	
	public void setUp(int noPins) {
		this.noPins = noPins;
	}
	
	public void takePins(int pinsToTake) {
		noPins -= pinsToTake;
	}
	
	public int getNoPins() {
		return noPins; 
	}
}
