/*
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Note in this situation -121 backward is 121- and that is not a palindrome.
*/

public boolean isPalindrome(int x) {
        
        String number = Integer.toString(x);
        int length = number.length();
        
        StringBuilder sb = new StringBuilder();
        while(length!=0){
            sb.append(number.charAt(length-1));
            length--;
        }
        String reversed = sb.toString();
        if(number.equals(reversed)) return true;
         
        return false;
    }

//Alternative Solution 

 public boolean isPalindrome(int x) {
        
        String number = Integer.toString(x);
        StringBuilder sb = new StringBuilder(number);
        sb.reverse();
        String reversed = sb.toString();
        
        if(number.equals(reversed)) return true;
        
        return false;
}
