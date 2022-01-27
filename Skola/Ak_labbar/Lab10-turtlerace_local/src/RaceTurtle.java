import java.util.Random;

public class RaceTurtle extends Turtle {
    private RaceWindow w;
    private int nbr;
    private Random rand = new Random();


    public RaceTurtle(RaceWindow w, int nbr){
        super(w, RaceWindow.getStartXPos(nbr), RaceWindow.getStartYPos(nbr) );
        this.nbr = nbr;
        this.w = w;
        left(270);
        penDown();
    }

    public void raceStep(){
        int stepDistance = rand.nextInt(5) + 1;
        forward(stepDistance);
    }

    public String toString(){
        return "Nummer " + nbr; 
    }
}
