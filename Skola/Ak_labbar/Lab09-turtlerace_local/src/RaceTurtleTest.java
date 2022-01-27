import java.util.ArrayList;

public class RaceTurtleTest {
	public static void main(String[] args) {
		RaceWindow w = new RaceWindow();

		ArrayList<RaceTurtle> turtles = new ArrayList<RaceTurtle>();
		for (int i = 1; i <= 8; i++) {
			turtles.add(new RaceTurtle(w, i));
		}
		
		ArrayList<RaceTurtle> completedTurtles = new ArrayList<RaceTurtle>();
		while(completedTurtles.size() < 8) {

			for (RaceTurtle r : turtles) {
				if(completedTurtles.contains(r)) {continue;}
				if (r.getX() >= RaceWindow.X_END_POS) {
					completedTurtles.add(r);
				} else {
					r.raceStep();
				}
			}
			RaceWindow.delay(20);
		}
		
		for (int i = 0; i < 3; i++) {
			String turtleN = completedTurtles.get(i).toString();
			String toPrint = "På plats " + (i+1) + ": " + turtleN;
			System.out.println(toPrint);
		}
	}
}
