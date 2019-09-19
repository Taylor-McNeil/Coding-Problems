//We are using the ACSII codes here to map our letters to numbers. The ASCII code for A is 97.

static int makingAnagrams(String s1, String s2) {

        int [] differences = new int[26];
        int total=0;
        
        for(int i=0;i<s1.length();i++){differences[s1.charAt(i)-97]++;}
        for(int j=0;j<s2.length();j++){differences[s2.charAt(j)-97]--;}
        
        for(int i=0;i<26;i++){total += Math.abs(differences[i]);}
return total;
    }


/*
        We can use a for each loop here.
        for(char characterA : s1.toCharacterArray()){differences[characterA-97]++;}
        for(char characterB : s2.toCharacterArray()){differences[characterB-97]--;}
        for(int i: differences)(total += Math.abs(i);
        
        */
