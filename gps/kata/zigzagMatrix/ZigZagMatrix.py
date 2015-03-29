__author__ = 'Sony'


class ZigzagMatrix(object):
    @classmethod
    def sort(cls, param):
        startSubMatrix = ["1,1"]
        if param > 1:
            counter = 2
            while counter <= param:
                if counter % 2 == 0:
                    xIndex = 1
                    yIndex = counter
                    while xIndex <= counter:
                        startSubMatrix.append(str(xIndex) + "," + str(yIndex))
                        yIndex -= 1
                        xIndex += 1
                else:
                    xIndex = counter
                    yIndex = 1
                    while xIndex >= 1:
                        startSubMatrix.append(str(xIndex) + "," + str(yIndex))
                        yIndex += 1
                        xIndex -= 1
                counter += 1
        if param % 2 == 0:
            for counterSufixMatrix in range(2, param + 1):
                if counterSufixMatrix % 2 == 0:
                    xIndex = param
                    yIndex = counterSufixMatrix
                    while yIndex <= param:
                        startSubMatrix.append(str(xIndex) + "," + str(yIndex))
                        xIndex -= 1
                        yIndex += 1
                else:
                    xIndex = counterSufixMatrix
                    yIndex = param
                    while xIndex <= param:
                        startSubMatrix.append(str(xIndex) + "," + str(yIndex))
                        xIndex += 1
                        yIndex -= 1
        else:
            for counterSufixMatrix in range(2, param + 1):
                if counterSufixMatrix % 2 == 0:
                    xIndex = counterSufixMatrix
                    yIndex = param
                    while xIndex <= param:
                        startSubMatrix.append(str(xIndex) + "," + str(yIndex))
                        xIndex += 1
                        yIndex -= 1
                else:
                    xIndex = param
                    yIndex = counterSufixMatrix
                    while yIndex <= param:
                        startSubMatrix.append(str(xIndex) + "," + str(yIndex))
                        xIndex -= 1
                        yIndex += 1
        return startSubMatrix