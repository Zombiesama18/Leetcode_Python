# 1603. 设计停车系统
# 请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。
# 请你实现ParkingSystem类：
# ParkingSystem(int big, int medium, int small)初始化ParkingSystem类，三个参数分别对应每种停车位的数目。
# bool addCar(int carType)检查是否有carType对应的停车位。carType有三种类型：大，中，小，分别用数字1，2和3表示。一辆车只能停在carType对应
# 尺寸的停车位中。如果没有空车位，请返回false，否则将该车停入车位并返回true。
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.maxNum = [big, medium, small]
        self.currentNum = [0, 0, 0]

    def addCar(self, carType: int):
        if carType < 1 or carType > 3:
            return False
        if self.currentNum[carType - 1] == self.maxNum[carType - 1]:
            return False
        else:
            self.currentNum[carType - 1] += 1
            return True


parkingSystem = ParkingSystem(1, 1, 0)
parkingSystem.addCar(1)
parkingSystem.addCar(2)
parkingSystem.addCar(3)
parkingSystem.addCar(1)
