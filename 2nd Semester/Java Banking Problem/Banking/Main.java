package Banking;

import java.util.Hashtable;
import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Bank b = new Bank("BCA");
        Scanner scanner = new Scanner(System.in);
        int id = 0;

        Hashtable<String, String> user = new Hashtable<String, String>();
        Hashtable<String, Double> memberlist = new Hashtable<String, Double>();
        Hashtable<String, Integer> memberid = new Hashtable<String, Integer>();
        user.put("staff staff","12345");

        int i = 0;
        while (i==0)
        {
            System.out.println("\nWelcome to the Bank");

            System.out.print("Do You Have an Account(Yes or No)?: ");
            String yn = scanner.next();

            if (yn.equals("No"))
            {
                System.out.println("Please Register Your New Account.");

                System.out.print("Please Input Your First Name: ");
                String firstName = scanner.next();
                System.out.print("Please Input Your Last Name: ");
                String lastName = scanner.next();
                System.out.print("Please Input Your Password: ");
                String password = scanner.next();
                Customer c = new Customer(firstName, lastName);

                String dict = c.getFirstName() +" "+ c.getLastName();
                user.put(dict, password);
                b.addCustomer(firstName, lastName);
                id+=1;
                memberid.put(dict, id);

                if (!user.contains(dict))
                {
                    double balance = 0;
                    memberlist.put(dict,balance);
                }

                double bal = Double.parseDouble(user.get(dict));

                Account a = new Account(bal);
                c.setAccount(a);

                System.out.println("Your Account has been Registered.\n");

            }

            System.out.println("Please Login to Your Account.");

            System.out.print("Please Input Your First Name: ");
            String firstName = scanner.next();
            System.out.print("Please Input Your Last Name: ");
            String lastName = scanner.next();
            System.out.print("Please Input Your Password: ");
            String password = scanner.next();
            String username = firstName+" "+lastName;

            if (user.containsKey("staff staff") && password.equals(user.get("staff staff")))
            {
                System.out.println("Welcome Staff");
                int loop = 0;
                label:
                while (loop == 0)
                {
                    System.out.print("\nMenu\n1.Get Customer Account\n2.Number Of Customer\n3.Get Customer Index\n4.Quit\nPlease Pick a Number: ");
                    String number = scanner.next();

                    switch (number)
                    {
                        case "1":
                            System.out.print("Please Input Your First Name: ");
                            String firstn = scanner.next();
                            System.out.print("Please Input Your Last Name: ");
                            String lastn = scanner.next();
                            String users = firstn+" "+lastn;
                            System.out.println("Customer's Balance: "+memberlist.get(users));
                            break;
                        case "2":
                            System.out.println("Number of Customer is "+b.getNumberOfCustomers());
                            break;
                        case "3":
                            System.out.print("Please Input Your First Name: ");
                            String first = scanner.next();
                            System.out.print("Please Input Your Last Name: ");
                            String last = scanner.next();
                            String inp = first+" "+last;
                            System.out.println("Customer Index of "+inp+" is "+memberid.get(inp));
                            break;
                        case "4":
                            System.out.println("Thankyou for Using Our Service");
                            break label;
                    }
                }
            }

            else if (user.containsKey(username) && password.equals(user.get(username)))
            {
                System.out.println("\nYou have successfully login.");
                System.out.println("Welcome " + username);

                int loop = 0;
                label:
                while (loop == 0)
                {
                    System.out.print("\nMenu\n1.Balance\n2.Deposit\n3.Withdraw\n4.Quit\nPlease Pick a Number: ");
                    String number = scanner.next();

                    Account a = new Account(memberlist.get(username));

                    switch (number)
                    {
                        case "1":
                            System.out.print("Your Balance: "+a.getBalance()+"\n");
                            break;
                        case "2":
                            System.out.print("Please Input Amount of Deposit: ");
                            double depos = scanner.nextDouble();
                            a.deposit(depos);
                            if (depos>0) memberlist.put(username, memberlist.get(username)+depos);
                            System.out.println("Your Balance has been Added");
                            System.out.println("Your Balance: "+a.getBalance());
                            break;
                        case "3":
                            System.out.print("Please Input Amount of Withdraw: ");
                            double draw = scanner.nextDouble();
                            a.withdraw(draw);
                            if (draw>0) memberlist.put(username, memberlist.get(username)-draw);
                            System.out.println("Your Balance has been Withdrawn");
                            System.out.println("Your Balance: "+a.getBalance());
                            break;
                        case "4":
                            System.out.println("Thankyou for Using Our Service");
                            break label;
                    }
                }
            }

            else if (!user.containsKey(username) && !password.equals(user.get(username)))
            {
                System.out.println("No Data Is Found, Please Try Again.");
            }

            else System.out.println("Your Credentials are Wrong.");


        }
    }
}
