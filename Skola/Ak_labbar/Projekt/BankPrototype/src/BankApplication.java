import java.util.ArrayList;
import java.util.Scanner;

public class BankApplication {
    private Scanner scan = new Scanner(System.in);
    private Bank bank = new Bank();

    public static void main(String[] args) throws Exception {
        BankApplication myBankApp = new BankApplication();
        myBankApp.runApplication();
    }

    public void runApplication(){
        /*
        bank.addAccount("Doris Kruth", Long.parseLong("4111194444"));
        bank.addAccount("Charles Ingvar Jönsson", Long.parseLong("3705209999"));
        bank.addAccount("Jakob Morgan Rockefeller Wall-Enberg, Jr.", Long.parseLong("2306207777"));
        bank.addAccount("Jakob Morgan Rockefeller Wall-Enberg, Jr.", Long.parseLong("2306207777"));
        */
        boolean run = true;
        while (run){
            printChoices();
            System.out.print("val: ");
            String choice = scan.next();
            switch (choice) {
                case "1":
                    findAccountsForHolder();
                    break;
                case "2":
                    findByPartOfName();
                    break;
                case "3":
                    depositOnly();
                    break;
                case "4":
                    withdrawOnly();
                    break;
                case "5":
                    transfer();
                    break;
                case "6":
                    createAccount();
                    break;
                case "7":
                    removeAccount();
                    break;
                case "8":
                    getAccounts();
                    break;
                case "9":
                    run = false;
                    break;
                default:
                    System.out.println("Vänligen välj ett riktigt alternativ");
                    break;
            }
        }
    }


    private void findAccountsForHolder() {
        System.out.print("id: ");
        long idNr = Long.parseLong(scan.next());
        ArrayList<BankAccount> accounts = bank.findAccountsForHolder(idNr);
        for (BankAccount bankAccount : accounts) {
            System.out.println(bankAccount.toString());
        }
    }

    private void findByPartOfName() {
        System.out.print("namn: ");
        String partOfName = "";
        while (partOfName.equals("")){
            partOfName = scan.nextLine();
        }
        ArrayList<BankAccount> accounts = bank.findByPartOfName(partOfName);
        for (BankAccount account : accounts) {
            System.out.println(account.toString());
        }
    }
    
    private void depositOnly(){
        System.out.print("konto: ");
        int accountNumber = Integer.parseInt(scan.next());
        System.out.print("belopp: ");
        double amount = Double.parseDouble(scan.next());
        deposit(accountNumber, amount);
    }

    private void withdrawOnly(){
        System.out.print("konto: ");
        int accountNumber = Integer.parseInt(scan.next());
        System.out.print("belopp: ");
        double amount = Double.parseDouble(scan.next());
        withdraw(accountNumber, amount);
    }


    private void transfer() {
        System.out.print("från konto: ");
        int accountNumber1 = Integer.parseInt(scan.next());

        System.out.print("till konto: ");
        int accountNumber2 = Integer.parseInt(scan.next());

        System.out.print("belopp: ");
        double amount = Double.parseDouble(scan.next());

        boolean withdrawSuccess = withdraw(accountNumber1, amount);
        if (withdrawSuccess){
            boolean depositSuccess = deposit(accountNumber2, amount);
            if (depositSuccess){
                System.out.println("Överföring var lyckad!");
            } else {
                deposit(accountNumber1, amount);
            }
        }

    }


    private boolean deposit(int accountNumber, double amount) {
        BankAccount account = bank.findByNumber(accountNumber); 
        if (account == null){
            System.out.println("Konto finns ej");
        } else {
            
            if (amount < 0){
                System.out.println("Kan inte sätta in en negativ mängd");
            } else {
                account.deposit(amount);  
                System.out.println(account.toString());
                return true;
            }
        }
        return false;
    }


    private boolean withdraw(int accountNumber, double amount) {
        BankAccount account = bank.findByNumber(accountNumber); 
        if (account == null) {
            System.out.println("Konto finns ej");
        } else {
            double balance = account.getBalance();
            if (amount < 0){
                System.out.println("Kan inte ta ut en negativ mängd");
            } else if (amount > balance) {
                System.out.println("Uttaget misslyckades, endast " + balance + " på kontot!");
            } else {
                account.withdraw(amount);
                System.out.println(account.toString());
                return true;
            }
        }
        return false;
    }

    private void createAccount() {
        System.out.print("namn: ");
        String name = "";
        while (name.equals("")){
            name = scan.nextLine();
        }
        System.out.print("id: ");
        long idNr = Long.parseLong(scan.next());
        int accountNr = bank.addAccount(name, idNr);
        System.out.println("konto skapat: " + accountNr);
    }

    private void removeAccount() {
        System.out.print("konto: ");
        int accountNr = Integer.parseInt(scan.next());
        boolean result = bank.removeAccount(accountNr); 
        if (!result){
            System.out.println("Konto finns ej!");
        }
    }

    private void getAccounts() {
        ArrayList<BankAccount> accounts = bank.getAllAccounts();
        for (BankAccount bankAccount : accounts) {
            System.out.println(bankAccount.toString());
        }
    }

    public void printChoices(){
        
        String[] toPrint = {"----------------------------------------------------------",
        "1. Hitta konto utifrån innehavare",
        "2. Sök kontoinnehavare utifrån (del av) namn",
        "3. Sätt in",
        "4. Ta ut",
        "5. Överföring",
        "6. Skapa konto",
        "7. Ta bort konto",
        "8. Skriv ut konton",
        "9. Avsluta"};

        for (int i = 0; i < toPrint.length; i++) {
            System.out.print(toPrint[i] + "\n");
        }
    }

}
