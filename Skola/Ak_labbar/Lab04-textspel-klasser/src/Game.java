import java.util.Scanner;
import se.lth.cs.pt.timer.Timer;
import java.util.Random;

public class Game {

	public static void main(String[] args) {
		while (true){
			System.out.println("Get ready for a random character!");
			Random rand = new Random();
			long randomTime = 1000 + 1000 * rand.nextInt(10);
			Timer.delay(randomTime); 
			
			char charToPrint = getRandomChar();
			System.out.println(charToPrint);
			char firstChar = ' ';
			Scanner scan = new Scanner(System.in);
			long start = System.nanoTime();
			boolean whileBreak = false;
			while (firstChar != charToPrint){
				String inputString = scan.next();
				if (compareStrings(inputString, "exit")) {
					whileBreak = true;
					break;
				}
				firstChar = inputString.charAt(0);
			}

			if (whileBreak){
				break;
			}

			long stop = System.nanoTime();
			System.out.println((stop - start)/1000000 + " ms");
		}	
		
	}

	public static char getRandomChar(){
		char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
		Random rand = new Random();
		int randomIndex = rand.nextInt(alphabet.length);
		return alphabet[randomIndex];
	}

	public static boolean compareStrings(String str1, String str2){
		if (str1.length() != str2.length()) {
			return false;
		}

		for (int i = 0; i < str1.length(); i++){
			if (str1.charAt(i) != str2.charAt(i)){
				return false;
			}
		}
		return true;
	}

}
