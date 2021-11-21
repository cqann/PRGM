import se.lth.cs.pt.window.SimpleWindow;
import se.lth.cs.pt.square.Square;

public class StepSquare {
	public static void main(String[] args) {
		SimpleWindow w = new SimpleWindow(600, 600, "RedrawSquare");
		int lastX = 0;
		int lastY = 0;
		float steps = 10;
		while (true) {
			w.waitForMouseClick();
			w.clear();
			int x = w.getMouseX();
			int y = w.getMouseY();
			int deltaX = x - lastX;
			int deltaY = y - lastY;
			for (int i = 0; i < steps; i++){
				int sqX = (int) (lastX + i * (deltaX / steps));
				int sqY = (int) (lastY + i * (deltaY / steps));
				Square sq = new Square(sqX, sqY, 100);
				sq.draw(w);
			}
			lastX = x;
			lastY = y;
		}
		
	}
}
