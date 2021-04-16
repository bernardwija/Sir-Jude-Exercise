package Banking;

import java.util.ArrayList;

public class Bank
{
    private java.util.ArrayList<Customer> customers = new java.util.ArrayList<>();
    private int numberOfCustomers;
    private final String bankName;

    public Bank(String bankName)
    {
        this.bankName = bankName;
    }

    public void addCustomer (String firstName, String lastName)
    {
        customers.add(new Customer(firstName, lastName));
        numberOfCustomers++;
    }

    public int getNumberOfCustomers()
    {
        return numberOfCustomers;
    }

    public Customer getCustomers(int index)
    {
        return customers.get(index);
    }
}
