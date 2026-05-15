class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        hand = sorted(hand)
        hashmap = {}
        for i in hand:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1
        minval = min(hashmap.keys())
        for i in range(1,len(hand)+1):
            if minval in hashmap.keys():
                hashmap[minval]-=1
                if hashmap[minval] == 0:
                    del hashmap[minval]
                print(minval)
                print(hashmap)
                minval +=1
            else:
                return False
            
            if i % groupSize ==0 and len(hashmap.keys())!=0:
                minval = min(hashmap.keys())
        return True


        
