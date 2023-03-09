def twoSum(nums, target: int):
	indices = []
	for i in range(len(nums)-1):
		for j in range(len(nums)):
			if i < j :
				if target == nums[i] + nums[j]:
					indices.append(i)
					indices.append(j)
	return indices
