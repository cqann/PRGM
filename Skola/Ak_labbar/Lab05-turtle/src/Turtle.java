import se.lth.cs.pt.window.SimpleWindow;
import java.lang.Math;

//Attribut är "dir"
//parameter är "n" i metoden forward
// En lokal variabel är "radDir" i metoden forward

public class Turtle {
	private SimpleWindow w; //innehålller fönstret som turteln befinner sig på
	private double x; //nuvarnde xpos
	private double y;  //nuvarande ypos
	private int dir; //direction in degrees
	private boolean drawing = false; //är pennan nere? dvs ritar vi?

	/** Skapar en sköldpadda som ritar i ritfönstret w. Från början 
	    befinner sig sköldpaddan i punkten x, y med pennan lyft och 
	    huvudet pekande rakt uppåt i fönstret (i negativ y-riktning). */
	public Turtle(SimpleWindow w, int x, int y) {
		this.w = w; 
		this.x = x; 
		this.y = y;
		this.dir = 90;
		w.moveTo(x, y);
	}

	public static void main(String[] args) {
		
	}
	/** Sänker pennan. */
	public void penDown() {
		drawing = true;
	}
	
	/** Lyfter pennan. */
	public void penUp() {
		drawing = false;
	}
	
	/** Går rakt framåt n pixlar i den riktning huvudet pekar. */
	public void forward(int n) {
		move();
		double radDir = dir * (Math.PI/180);
		double dx = n * Math.cos(radDir);
		double dy = n * Math.sin(radDir);
		x += dx;
		y -= dy;
		if (drawing) line(); else move();
	}

	/** Vrider beta grader åt vänster runt pennan. */
	public void left(int beta) {
		dir += beta;
		dir %= 360;
	}

	/** Går till punkten newX, newY utan att rita. Pennans läge (sänkt
	    eller lyft) och huvudets riktning påverkas inte. */
	public void jumpTo(int newX, int newY) {
		x = newX;
		y = newY;
	}

	/** Återställer huvudriktningen till den ursprungliga. */
	public void turnNorth() {
		dir = 90;
	}

	/** Tar reda på x-koordinaten för sköldpaddans aktuella position. */
	public int getX() {
		return (int) Math.round(x);
	}

 	/** Tar reda på y-koordinaten för sköldpaddans aktuella position. */
	public int getY() {
		return (int) Math.round(y);
	}
  
	/** Tar reda på sköldpaddans riktning, i grader från den positiva X-axeln. */
 	public int getDirection() {
 		return (int) Math.round(dir);
	}

	private void line(){
		w.lineTo((int) Math.round(x), (int) Math.round(y));
	}

	private void move(){
		w.moveTo((int) Math.round(x), (int) Math.round(y));
	}
}
