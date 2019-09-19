//Reverse an array

  static int[] reverseArray(int[] a) {

        int temp=0;
        int index=a.length-1;
     
        
        for(int i=0;i<a.length/2;i++){
            temp = a[i];
            a[i]=a[index-i];
            a[index-i]=temp;
        }

  // Runtime: O(n)
