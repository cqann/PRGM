import se.lth.cs.pt.window.SimpleWindow;
import se.lth.cs.pt.square.Square;

public class RedrawSquare {
	public static void main(String[] args) {
		SimpleWindow w = new SimpleWindow(600, 600, "RedrawSquare");
		while (true) {
			w.waitForMouseClick();
			w.clear();
			Square sq = new Square(w.getMouseX(), w.getMouseY(), 100);
			sq.draw(w);
		}
		
	}
}
