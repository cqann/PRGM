import java.util.ArrayList;
import java.util.Random;

public class RaceTurtleTest {
	public static void main(String[] args) {
		RaceWindow w = new RaceWindow();
		Random rand = new Random();


		ArrayList<RaceTurtle> turtles = new ArrayList<RaceTurtle>();
		for (int i = 1; i <= 8; i++) {
			int type = rand.nextInt(3);
			RaceTurtle turtle;
			if (type == 0){
				turtle = new MoleTurtle(w, i);
			} else if(type == 1) {
				int absentness = rand.nextInt(100) + 1;
				turtle = new AbsentMindedTurtle(w, i, absentness);
			} else {
				int dizzyness = rand.nextInt(5) + 1;
				turtle = new DizzyTurtle(w, i, dizzyness);
			}
			turtles.add(turtle);
			System.out.println(turtle.toString());
		}
		
		ArrayList<RaceTurtle> completedTurtles = new ArrayList<RaceTurtle>();
		while(completedTurtles.size() < 8) {

			for (RaceTurtle r : turtles) {
				if( completedTurtles.contains(r)) {continue;}
				if (r.getX() >= RaceWindow.X_END_POS) {
					completedTurtles.add(r);
				} else {
					r.raceStep();
				}
			}
			RaceWindow.delay(5);
		}
		
		for (int i = 0; i < 3; i++) {
			String turtleN = completedTurtles.get(i).toString();
			String toPrint = "På plats " + (i+1) + ": " + turtleN;
			System.out.println(toPrint);
		}
	}
}
