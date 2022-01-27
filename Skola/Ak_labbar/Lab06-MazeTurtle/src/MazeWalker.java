import se.lth.cs.pt.window.SimpleWindow;
import se.lth.cs.pt.maze.Maze;
import java.util.Scanner;

public class MazeWalker {
    public static void main(String[] args) throws Exception {
        SimpleWindow w = new SimpleWindow(400, 400, "MazeWalker");
        Scanner scan = new Scanner(System.in);
        int mazeN = Integer.parseInt(scan.next());
        Maze maze = new Maze(mazeN);
        maze.draw(w);
        scan.close();
        Turtle t = new Turtle(w, maze.getXEntry(), maze.getYEntry()); 
        t.penDown();
        
        while (!maze.atExit(t.getX(), t.getY())){
            SimpleWindow.delay(1);
            boolean left = maze.wallAtLeft(t.getDirection(), t.getX(), t.getY());
            boolean forward = maze.wallInFront(t.getDirection(), t.getX(), t.getY());

            if (!left){
                t.left(90);
                t.forward(1);
                continue;
            }
            if (!forward){
                t.forward(1);
            } else {
                t.left(-90);
            }

            
        }
    }
}
