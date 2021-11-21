import se.lth.cs.pt.window.SimpleWindow;

public class LineDrawing {

	public static void main(String[] args) {
		SimpleWindow w = new SimpleWindow(500, 500, "LineDrawing");
		w.moveTo(0, 0);
		int n = 0;
		while (true) {
			w.waitForMouseClick();

			int x = w.getMouseX();
			int y = w.getMouseY();
			if (n == 0) {
				w.moveTo(x,y);
			} else {
				w.lineTo(x,y);
			}
			n++;
		}
	}
}
