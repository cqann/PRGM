public class Customer {
    private String name;
    private long idNr;
    private int customerId;

    public Customer(String name, long idNr, Bank bank){
        this.name = name;
        this.idNr = idNr;
        this.customerId = bank.nextCustomerId();
    }

    public String getName(){
        return name;
    }

    public long getIdNr(){
        return idNr;
    }

    public int getCustomerId(){
        return customerId;
    }

    public String toString(){
        return name + ", id " +  idNr + ", kundnr " + customerId;
    }
}
