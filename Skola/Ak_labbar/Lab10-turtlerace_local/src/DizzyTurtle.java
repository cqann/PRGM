import java.util.Random;

public class DizzyTurtle extends RaceTurtle{
    private Random rand = new Random();
    private int dizzyness;
    
    public DizzyTurtle(RaceWindow w, int nbr, int dizzyness){
        super(w, nbr);
        this.dizzyness = dizzyness;
    }

    public void raceStep(){
        double turn = (rand.nextDouble() - 0.5) * (dizzyness / 5.0) * 15;
        left((int) turn);
        super.raceStep();
        
    }

    public String toString(){
        return super.toString() + " - DizzyTurtle (Yrsel: " + dizzyness + ")";
    }
}
