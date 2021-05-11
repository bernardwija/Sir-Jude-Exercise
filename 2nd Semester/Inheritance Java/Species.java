package ZooBer;

import java.util.LinkedList;

public class Species extends Genus {
    private String speciesName;

    public Species(String s, String g) {
        super(g);
        setSpeciesName(s);
    }

    public void setSpeciesName(String s) {
        speciesName = s;
    }

    public String getSpeciesName() {
        return speciesName;
    }

    public String toString() {
        return "Species: " + getGenusName() + " " + speciesName;
    }

    public boolean equals(Species s) {
        return speciesName.equals(s.getSpeciesName());
    }

    //IV.C
    public static LinkedList<Species> makeSpeciesList(LinkedList<Specimen> animals) {
        LinkedList<Species> speciesList = new LinkedList<Species>();
        for (Specimen animal: animals) {
            speciesList.add(animal.getTOA());
        }
        return speciesList;
    }

    //IV.D
    public static LinkedList<Species> makeSpeciesListUnique(LinkedList<Species> allSpecies) {
        LinkedList<Species> speciesListUnique = new LinkedList<Species>();
        for (Species species: allSpecies) {
            if (!speciesListUnique.contains(species)) {
                speciesListUnique.add(species);
            }
        }
        return speciesListUnique;
    }

    listSpecies (Specimen[] animals){
        LinkedList<String> speciesList = new LinkedList <String>();
        for (each animal in animals){
            if (animal's species has not existed in speciesList){
                    insert animal's species into species"ist
        }
        return allSpecies;
    }
}
