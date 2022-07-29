/*506. Relative Ranks

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:
                                                                                  
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].*/

class Solution 
{
    public String[] findRelativeRanks(int[] score) 
    {
        String [] ans=new String[score.length];
        int [] sortedArray=new int[score.length];
        for(int i=0; i<score.length; i++)
            sortedArray[i]=score[i];
        Arrays.sort(sortedArray);
        HashMap<Integer,String> map=new HashMap<>();
        for(int i=0; i<sortedArray.length; i++)
        {
            if(i==sortedArray.length-3)
                map.put(sortedArray[i], "Bronze Medal");
            else if(i==sortedArray.length-2)
                map.put(sortedArray[i], "Silver Medal");
            else if(i==sortedArray.length-1)
                map.put(sortedArray[i], "Gold Medal");
            else
                map.put(sortedArray[i], String.valueOf(sortedArray.length-i));
        }
        for(int i=0; i<score.length; i++)
            ans[i]=map.get(score[i]);
        return ans;
    }
}
