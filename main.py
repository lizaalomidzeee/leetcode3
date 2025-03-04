def arrayPairSum(nums):
    nums.sort()
    return sum(nums[i] for i in range(0, len(nums), 2))


#example 
nums1 = [1, 4, 3, 2]
print(arrayPairSum(nums1)) 


# პირველ რიგში თანმიმდევრობით ვალაგებთ რიცხვებს, შემდეგ ვყოფთ ორ-ორ წყვილად და ვუმატებთ ერთმანეთს, რის შედეგადაც საბოლოოდ ვიღებთ მაქსიმალურ ჯამს