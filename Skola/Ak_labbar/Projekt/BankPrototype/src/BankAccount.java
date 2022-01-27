public class BankAccount {
    private Customer holder;
    private int accntNr;
    private double balance;

    public BankAccount(String holderName, long holderId, Bank bank){
        this.holder = new Customer(holderName, holderId, bank);
        this.accntNr = bank.nextAccntNr();
        this.balance = 0;
    }

    public BankAccount(Customer holder, Bank bank) {
        this.holder = holder;
        this.accntNr = bank.nextAccntNr();
        this.balance = 0;
    }

    public Customer getHolder(){
        return holder;
    }

    public int getAccountNumber(){
        return accntNr;
    }

    public double getBalance(){
        return balance;
    }

    public void deposit(double amount){
        balance += amount;
    }

    public void withdraw(double amount){
        balance -= amount;
    }

    public String toString(){
        return "konto " + accntNr + " (" + holder.toString() + "): " + balance;
    }



}
