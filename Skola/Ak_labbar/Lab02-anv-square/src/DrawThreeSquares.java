import se.lth.cs.pt.window.SimpleWindow;
import se.lth.cs.pt.square.Square;

public class DrawThreeSquares {
	public static void main(String[] args) {
		SimpleWindow w = new SimpleWindow(600, 600, "DrawSquare");
		Square sq1 = new Square(250, 250, 100);
		Square sq2 = new Square(300, 230, 100);
		Square sq3 = new Square(270, 270, 100);
		sq1.draw(w);
		sq2.draw(w);
		sq3.draw(w);

	}
}
