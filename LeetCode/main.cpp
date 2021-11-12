//
//  main.cpp
//  LeetCode
//
//  Created by Leo  Innocenzi on 12/11/2021.
//

#include <iostream>
#include <vector>

#define NELEMS(x) (sizeof(x)/sizeof((x)[0]))

class Solution {

public:
    
    void swap(int *xp, int *yp) {
        int temp = *xp;
        *xp = *yp;
        *yp = temp;
    }
    
    double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
        
        std::vector<int> nums;
        int nums1Lenght = NELEMS(nums1);
        int nums2Lenght = NELEMS(nums2);
        
        for(int i=0; i<=nums2Lenght; i++) {
            nums = nums1;
            nums[nums1Lenght+i] = nums2[i];
        }
        
        int numsLenght = NELEMS(nums);
        int i,j;
        
        for(i=0; i<numsLenght; i++) {
            
            for(j=0; j<numsLenght-i; j++) {
                
                if(nums[j] > nums[j+1]) {
                    swap(&nums[j], &nums[j+1]);
                }
            }
        }
        
        double median=0;
        
        if (numsLenght%2 == 0) {
            median = nums[(numsLenght-1)/2];
        }
        else {
            median = (nums[(numsLenght-2)/2] + nums[(numsLenght-1)/2])/2;
        }
        
        return median;
    }
};


int main(int argc, const char * argv[]) {
    
    Solution s;
    std::vector<int> nums1 = {1,3};
    std::vector<int> nums2 = {2};
    
    double median = s.findMedianSortedArrays(nums1, nums2);
    std::cout << "Median is : " << median << std::endl;
    
    return 0;
}
