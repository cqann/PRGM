package rekrytering;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileReader {

	/**
	 * Returnerar max nbrOfRows rader från filen som en vektor av Applicant-objekt.
	 * Läser i filen tills det inte finns fler rader eller tills man läst nbrOfRows
	 * rader (det som inträffar först). 
	 * Returnerar null om filen inte finns.
	 */
	public static Applicant[] readFromFile(String fileName, int nbrOfRows) {
		Scanner scan;
		fileName = System.getProperty("user.dir") + "\\Lab07-rekrytering\\" + fileName;
		try {
			scan = new Scanner(new File(fileName), "utf-8");
		} catch (FileNotFoundException e) {
			System.err.println("File not found " + fileName);
			e.printStackTrace();
			return null;
		}
		Applicant[] applicants = new Applicant[nbrOfRows];
		int i = 0;
		while ( i < nbrOfRows){
			if (!scan.hasNext()){
				break;
			}
			String row = scan.nextLine();
			String[] row_split = row.split(" ");
			String full_name = row_split[0] + " " + row_split[1];
			String grade_string = row_split[2];
			applicants[i] = new Applicant(full_name, grade_string);
			i++;
		}
		//Här kan du använda Scannern för att läsa från filen fileName.
		//Varje rad motsvarar en Applicant. Kontrollera vad Applicants konstruktor kräver
		//Alla Applicant-objekt (max nbrOfRows stycken) ska lagras i en Applicant-vektor och returneras på slutet
		return applicants; //Byt ut denna rad mot hela lösningen
	}
}
