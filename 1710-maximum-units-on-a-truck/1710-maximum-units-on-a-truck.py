class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        x = sorted(boxTypes, key= lambda x:x[1], reverse=True)
        print(x)
        unit = 0
        box_count = 0
        for i in range(len(boxTypes)):
            
            if box_count+x[i][0] <= truckSize:
                unit += x[i][0]*x[i][1]
                box_count += x[i][0]
                
            else:
                box_required = truckSize - box_count
                unit += x[i][1]*box_required
                break
        return unit
                