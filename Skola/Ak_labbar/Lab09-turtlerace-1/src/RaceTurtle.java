import Turtle;

public class RaceTurtle extends Turtle {
    private RaceWindow w;
    private int nbr;


    public RaceTurtle(RaceWindow w, int nbr){
        super(w, (nbr+1) * 20, 30 );
        this.nbr = nbr;
        this.w = w;
    }
}
