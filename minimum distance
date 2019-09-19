 // Complete the minimumDistances function below.
    static int minimumDistances(int[] a) {

  int smallest = -1;
    ArrayList<Integer> al = new ArrayList<Integer>();
        
    for(int i=0;i<a.length;i++){
        for(int j=i+1;j<a.length;j++){
            if(a[i]==a[j]){
                int distance = Math.abs(j-i);
                al.add(distance);
            }
        }
    }
        Collections.sort(al);
        if(al.isEmpty()){
            return -1;
        }else{
            return al.get(0);
        }
    }
