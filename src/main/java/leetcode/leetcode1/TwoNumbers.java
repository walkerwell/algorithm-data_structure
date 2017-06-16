package leetcode.leetcode1;

import org.junit.Test;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by wubo on 2017-4-24.
 */
public class TwoNumbers {
    /**
     *
     Given an array of integers, return indices of the two numbers such that they add up to a specific target.

     You may assume that each input would have exactly one solution, and you may not use the same element twice.

     Example:

     Given nums = [2, 7, 11, 15], target = 9,

     Because nums[0] + nums[1] = 2 + 7 = 9,
     return [0, 1].

     *
     */
    @Test
    public void testRun (){
        int a [] = twoNum(new int[]{-1, 4, 3, 0}, 7);
        System.out.println(a[0]+" "+a[1]);
    }

    /**
     * O n 的时间复杂度
     * @param numbers
     * @param target
     * @return
     */
    public int[] twoNums(int [] numbers,int target){
        int [] result = new int [2];
        Map<Integer,Integer> map = new HashMap();
        for(int i =0 ;i<numbers.length;i++){
            if(map.containsKey(target - numbers[i])){
                result[0] = map.get(target - numbers[i]);
                result[1] = i;
                break;
            }
            /** 目的是为了获取 numbers[i] 和 其下标 i  **/
            map.put(numbers[i],i);
        }
        return result;
    }

    public int[] twoNum(int [] numbers,int target){
        int res [] = new int[2];
        Map<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<numbers.length;i++){
            if(map.containsKey(numbers[i])){
                res [0] = map.get(numbers[i]);
                res [1] = i;
                break;
            }
            map.put(target - numbers[i],i);
        }
        return res;
    }

    /**
     * O n * n 的时间复杂度
     * @param numbers
     * @param target
     * @return
     */
    public int[] BF(int [] numbers,int target){
        int result [] = new int[2];
        for(int i=0 ;i<numbers.length-2;i++){
            for(int j=i;j<numbers.length-1;j++){
                if(numbers[i] + numbers[j] == target){
                    result[0] = i;
                    result[1] = j;
                    break;
                }
            }
        }
        return result;
    }
}
