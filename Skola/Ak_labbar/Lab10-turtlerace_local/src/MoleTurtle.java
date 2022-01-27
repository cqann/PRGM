import java.util.Random;

public class MoleTurtle extends RaceTurtle{
    private Random rand = new Random();
    
    public MoleTurtle(RaceWindow w, int nbr){
        super(w, nbr);
    }

    public void raceStep(){
        double flip = rand.nextDouble();
        if (flip < 0.5){
            penUp();
        } else {
            penDown();
        }
        super.raceStep();
    }

    public String toString(){
        return super.toString() + " - MoleTurtle";
    }
}
