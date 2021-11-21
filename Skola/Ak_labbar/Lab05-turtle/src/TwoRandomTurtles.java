import se.lth.cs.pt.window.SimpleWindow;
import java.util.Random;
import java.awt.Color;

public class TwoRandomTurtles {
  	public static void main(String[] args) {
		SimpleWindow w = new SimpleWindow(600, 600, "TurtleDrawSquare");
		Turtle t1 = new Turtle(w, 250, 250);
		Turtle t2 = new Turtle(w, 350, 350);
		Random rand = new Random();
		int length = 0;
		int dir = 0;
		t1.penDown();
		t2.penDown();
		w.setLineWidth(3);
		while (turtleSqDist(t1, t2) >= (30 * 30)) {
			length = rand.nextInt(10) + 1;
			dir = rand.nextInt(361) - 180;
			w.setLineColor(new Color(30,200,255));
			t1.forward(length);
			t1.left(dir);

			length = rand.nextInt(10) + 1;
			dir = rand.nextInt(361) - 180;
			w.setLineColor(new Color(255,200,30));
			t2.forward(length);
			t2.left(dir);
			
			SimpleWindow.delay(1);
		}
	}

	private static double turtleSqDist(Turtle t1, Turtle t2){
		int x1 = t1.getX();
		int y1 = t1.getY();
		int x2 = t2.getX();
		int y2 = t2.getY();
		return Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2);
	}
}


