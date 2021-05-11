package ZooBer;

import java.util.Arrays;
import java.util.LinkedList;

public class Specimen
{
    private String name;
    private int cageNumber;
    private Species toa;

    public Specimen( String a, int c, Species s)
    {
        setName(a);
        setCage(c);
        setTOA(s);
    }

    public void setName(String a){
        name = a;
    }

    public void setCage(int c){
        cageNumber = c;
    }

    public void setTOA(Species s){
        toa = s;
    }

    public String getName(){
        return name;
    }

    public int getCage(){
        return cageNumber;
    }

    public Species getTOA(){
        return toa;
    }

    public String toString(){
        return name + " is a " + toa + " in cage " + cageNumber;
    }

    //III.B
    public static int countSpecimens(Specimen[] animals, Species s) {
        int count = 0;
        for (Specimen x: animals) {
            if (x.getTOA().getSpeciesName().equals(s.getSpeciesName())) {
                count++;
            }
        }
        return count;
    }

    // IV.B
    public static LinkedList<Specimen> makeList(Specimen[] animals) {
        return new LinkedList<Specimen>(Arrays.asList(animals));
    }
}