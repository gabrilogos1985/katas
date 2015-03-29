__author__ = 'Sony'


class ZigzagMatrix(object):
    @classmethod
    def sort(cls, param):
        startSubMatrix = "1,1"
        if param > 1:
            # twoSubMatrix = ";1,2;2,1"
            counter = 2
            while counter <= param:
                if counter % 2 == 0:
                    # twoSubMatrix = ""
                    xIndex = 1
                    yIndex = counter
                    while xIndex <= counter:
                        startSubMatrix += ";" + (str(xIndex) + "," + str(yIndex))
                        yIndex -= 1
                        xIndex += 1
                else:
                    # threeSubMatrix = twoSubMatrix
                    xIndex = counter
                    yIndex = 1
                    while xIndex >= 1:
                        startSubMatrix += ";" + (str(xIndex) + "," + str(yIndex))
                        yIndex += 1
                        xIndex -= 1
                counter += 1

        if (param == 2):
            startSubMatrix += (";2,2")

        # if param > 2:
        # # threeSubMatrix = twoSubMatrix + ";3,1;2,2;1,3"
        # threeSubMatrix = twoSubMatrix
        # xIndex = 3
        # yIndex = 1
        # while xIndex >= 1:
        # threeSubMatrix += ";" + (str(xIndex) + "," + str(yIndex))
        # yIndex += 1
        # xIndex -= 1

        if param == 3:
            startSubMatrix += (";2,3;3,2;3,3")
        # if param > 3:
        # fourSubMatrix = ""
        # xIndex = 1
        # yIndex = 4
        # while xIndex <= 4:
        # fourSubMatrix += ";" + (str(xIndex) + "," + str(yIndex))
        # yIndex -= 1
        # xIndex += 1
        # fourSubMatrix = threeSubMatrix + fourSubMatrix
        if param == 4:
            startSubMatrix += (";4,2;3,3;2,4;3,4;4,3;4,4")
        if param == 5:
            startSubMatrix += (";2,5;3,4;4,3;5,2;5,3;4,4;3,5;4,5;5,4;5,5")
        return [startSubMatrix]