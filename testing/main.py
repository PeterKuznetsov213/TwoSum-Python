def twoSum(nums,target):
           for i in range(len(nums)):
               x=i+1
               for n in range(len(nums)):

                   if nums[i]+nums[x]==target:

                        return(i,x)


# target=9
# nums=(2,7,11,15)
print(twoSum((3,2,4), 6))