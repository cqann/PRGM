import se.lth.cs.pt.window.SimpleWindow;
import se.lth.cs.pt.square.Square;

public class AnimatedSquare {
	public static void main(String[] args) {
		SimpleWindow w = new SimpleWindow(600, 600, "RedrawSquare");
		int lastX = 0;
		int lastY = 0;
		float steps = 50;
		Square sq = new Square(0, 0, 0);
		while (true) {
			w.waitForMouseClick();
			sq.erase(w);
			int x = w.getMouseX();
			int y = w.getMouseY();
			int deltaX = x - lastX;
			int deltaY = y - lastY;
			for (int i = 0; i < steps; i++) {
				sq.erase(w);
				int sqX = (int) (lastX + i * (deltaX / steps));
				int sqY = (int) (lastY + i * (deltaY / steps));
				sq = new Square(sqX, sqY, 100);
				sq.draw(w);
				SimpleWindow.delay(10);
			}
			lastX = x;
			lastY = y;
		}

	}
}
