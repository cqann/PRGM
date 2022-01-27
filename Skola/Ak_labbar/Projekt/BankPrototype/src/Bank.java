import java.util.ArrayList;

public class Bank {
    private ArrayList<BankAccount> accounts = new ArrayList<BankAccount>();
    private ArrayList<Customer> customers = new ArrayList<Customer>();
    private int nextCustomerId = 100;
    private int nextAccntNr = 1000;

    public int addAccount(String holderName, long idNr){
        Customer customer = findHolder(idNr);
        if (customer == null){
            customer = new Customer(holderName, idNr, this);
            customers.add(customer);
        }
        BankAccount newAccount = new BankAccount(customer, this);
        accounts.add(newAccount);
        return newAccount.getAccountNumber();
    }

    public Customer findHolder(long idNr){
        for (Customer customer : customers) {
            if (customer.getIdNr() == idNr){
                return customer;
            }
        }
        return null;
    }

    public boolean removeAccount(int number){
        int indexToRemove = -1;
        for (int i = 0; i < accounts.size(); i++) {
            BankAccount bankAccount = accounts.get(i);
            if (bankAccount.getAccountNumber() == number){
                indexToRemove = i;
                break;
            }
        }
        if (indexToRemove >= 0){
            accounts.remove(indexToRemove);
        }
        return indexToRemove >= 0;
    }

    public ArrayList<BankAccount> getAllAccounts(){
        
        ArrayList<BankAccount> sortedAccounts = new ArrayList<BankAccount>();
        ArrayList<BankAccount> accountsCopy = new ArrayList<BankAccount>(accounts);
        for (int i = 0; i < accounts.size(); i++){
            BankAccount minAccnt = accountsCopy.get(0);
            String lowestName = minAccnt.getHolder().getName();
            for (int j = 1; j < accountsCopy.size(); j++) {
                BankAccount currentAccnt = accounts.get(j);
              
                String currentAccntName = currentAccnt.getHolder().getName();
                if (currentAccntName.compareTo(lowestName) < 0){
                    lowestName = currentAccntName;
                    minAccnt = currentAccnt;
                }
            }
            sortedAccounts.add(minAccnt);
            accountsCopy.remove(minAccnt);
        }
        return sortedAccounts;
    }

    public BankAccount findByNumber(int accountNumber){
        for (BankAccount account : accounts) {
            if (account.getAccountNumber() == accountNumber){
                return account;
            }
        }
        return null;
    }

    public ArrayList<BankAccount> findAccountsForHolder(long idNr){
        ArrayList<BankAccount> toReturn = new ArrayList<BankAccount>();
        for (BankAccount bankAccount : accounts) {
            if (bankAccount.getHolder().getIdNr() == idNr){
                toReturn.add(bankAccount);
            }
        }
        return toReturn;
    }

    public ArrayList<BankAccount> findByPartOfName(String namePart){
        ArrayList<BankAccount> toReturn = new ArrayList<BankAccount>();
        for (BankAccount account : accounts) {
            Customer customer = account.getHolder();
            if (customer.getName().toLowerCase().contains(namePart.toLowerCase())){
                toReturn.add(account);
            }
        }
        return toReturn;
    }

    public int nextAccntNr(){
        nextAccntNr += 1;
        return nextAccntNr;
    }

    public int nextCustomerId(){
        nextCustomerId += 1;
        return nextCustomerId;
    }


}
