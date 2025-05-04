def canPlantFlowers(flowerbed, n):
    
    for i in range(len(flowerbed)):
        
        if (i-1 >= 0 and flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i+1 < len(flowerbed) and flowerbed[i+1] == 0):
            
            flowerbed[i] = 1
            n -= 1
    if n == 0:
        print(flowerbed)
        return True
    else:
        return False
        
        
print(canPlantFlowers([1,0,0,0,1], 2))