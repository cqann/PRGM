import se.lth.cs.pt.window.SimpleWindow;
import java.util.Random;

public class RandomSteps {
 	public static void main(String[] args) {
		SimpleWindow w = new SimpleWindow(600, 600, "TurtleDrawSquare");
		Turtle t = new Turtle(w, 300, 300);
		Random rand = new Random();
		int length = 0;
		int dir = 0;
		t.penDown();
		for (int i = 0; i < 1000; i++) {
			length = rand.nextInt(10) + 1;
			dir = rand.nextInt(361) - 180;
			t.forward(length);
			t.left(dir);
			SimpleWindow.delay(10);
		}
	}
}
