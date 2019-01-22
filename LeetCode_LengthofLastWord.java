/*
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.




*/

class Solution {
    public int lengthOfLastWord(String s) {
       s=s.trim();
        if(s.isEmpty()) return 0;
        
        int index = s.lastIndexOf(" ",s.length());
        return s.length()-index-1;
    }
}

//Fun Fact: As of 1/22/2019 this has the fastest runtime for all the Java online submissions for this problem :)
