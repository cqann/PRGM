import java.awt.Color;

import se.lth.cs.pt.window.SimpleWindow;

public class SimpleWindowExample {
    public static void main(String[] args) {
        SimpleWindow w = new SimpleWindow(500, 500, "Drawing Window");
        w.moveTo(100, 100);
        w.lineTo(150, 100);
        w.setLineWidth(4);
        double n = 0; 
        while (n < 1000){
            int r = (int) (127 + Math.cos(n)*120);
            int g = (int) (127 + Math.sin(n - Math.PI/4)*120); ;
            int b = (int) (127 + Math.sin(n)*120); 
            System.out.println(r);
            w.setLineColor( new Color(r,g, b));
            w.lineTo(w.getMouseX(), w.getMouseY());
            SimpleWindow.delay(10);
            n += 0.1;
        }
    }
}
