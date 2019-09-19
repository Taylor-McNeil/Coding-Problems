static int hourglassSum(int[][] arr) {

int largestHourglass=Integer.MIN_VALUE;
    
 // Why is the magic number 4??!!!!!!       
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            int sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];
            largestHourglass= Math.max(largestHourglass,sum);
        }
    }

    return largestHourglass;}
