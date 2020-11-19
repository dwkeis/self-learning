# to calculate the fee of different transport
class Bus():
    # to cal bus' fee
    def distance(self,km):
        count = 0
        if km <=10:
            count = 1

        elif km >10:
            count = 2
        count*=15
        print ("you are taking Bus, Fee is : " + str(count))

class MRT():
    # to cal MRT fee
    def distance(self,km):
        result = 0
        if km <=20:
            result = 20
        elif km >20:
            count = ((km-20) / 5) + 1
            result = 20 + 5 * count
        print ("you are taking MRT, Fee is : " + str(result))

class Factory:
    # define what transport you choose
    def travel(self,which):
        if which == 'Bus':
            return Bus()
        if which == 'MRT':
            return MRT()


if __name__ == '__main__':
    travel = Factory()
    travel.travel('MRT').distance(21)
    travel.travel('Bus').distance(2)
