names = ["An", "Bình", "Cường", "Đạt", "Hoàn", "Minh", "Nam", "Thảo", "Trung"]

def BinarySearch(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
    
    return -1

print(BinarySearch(names, "Nam"))