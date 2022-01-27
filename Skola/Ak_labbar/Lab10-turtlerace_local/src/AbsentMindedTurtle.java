import java.util.Random;

public class AbsentMindedTurtle extends RaceTurtle{
    private Random rand = new Random();
    private int absentness;
    
    public AbsentMindedTurtle(RaceWindow w, int nbr, int absentness){
        super(w, nbr);
        this.absentness = absentness;
    }

    public void raceStep(){
        double flip = rand.nextDouble();
        if (flip > (absentness / 100.0)){
            super.raceStep();
        } 
    }

    public String toString(){
        return super.toString() + " - AbsentMindedTurtle (" + absentness + "%) frånvarande";
    }
}
