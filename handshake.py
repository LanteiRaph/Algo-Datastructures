#Ten people are at a party including you, say that each person greets the other
#atleat once howmany handshakes are there in total
class Solution():
    def brutal(self,value):
        #Init empy list for output
        list = []
        #Each person will have value-1 handskaes
        for i in range(value):
            handshakes = value - 1
            list.append(handshakes)

        return sum(list) / 2

    def oneliner(self, value):
        x = int(value * (value-1))
        #Return
        return x /2

x = Solution()

value = 9

print(x.brutal(value))
print(x.oneliner(value))