import java.util.Arrays;
import java.math.*;

public class LeetCode_TwoSum {
    public static void main(String[]args){
        int [] a = {3,2,4};

        System.out.println(Arrays.toString(twoSum(a,6)));
    }
    public static int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++)
            {
                int temp=0;
                temp=nums[i]+nums[j];

                if(temp==target)
                    return new int [] {i,j};

                }
            }
        throw new IllegalArgumentException("No Solution");}
}
