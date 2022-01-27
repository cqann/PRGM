package rekrytering;

import java.util.ArrayList;
import java.util.Arrays;

public class FindBestCandidates {
	private static final double MIN_AVG_GRADE = 4.6;

	public static void main(String[] args) {
		// Läs från fil (Börja med "applications_small.txt), spara resultatet i en
		// vektor
		Applicant[] small_applicants = FileReader.readFromFile("applications_all.txt", 150);
		Applicant[] chosen_candidates = findBestCandidates(small_applicants);
		Arrays.sort(chosen_candidates);
		for (int i = 0; i < chosen_candidates.length; i++){
			System.out.println(chosen_candidates[i].toString());
		}
		// Skicka in Applicant-vektorn (som du fick i föregående steg) till metoden
		// findBestCandidiates (nedan)
		// Spara resultatet i en vektor

		// Printa resultatet från findBestCandidates

	}

	public static Applicant[] findBestCandidates(Applicant[] applicants) {
		// Hitta alla kandidater som har medelbetyg över MIN_AVG_GRADE
		// Lagra alla dessa kandidater i en vektor, returnera vektorn
		ArrayList<Applicant> result = new ArrayList<Applicant>();
		
		for (int i = 0; i < applicants.length; i++){
			Applicant current_applicant = applicants[i];
			if (current_applicant == null) {
				break;
			}
			if (current_applicant.getAvgGrade() > MIN_AVG_GRADE){
				result.add(current_applicant);
			}
		}
		Applicant[] array_result = result.toArray(new Applicant[0]);
		return array_result; 
	}
}
