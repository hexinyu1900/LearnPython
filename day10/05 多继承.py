class Horse:
    """马类"""
    def run(self):
        """跑方法"""
        print("马跑得快")

class Donkey:
    """驴类"""
    def walk(self):
        """走方法"""
        print("驴走得远")

class Mule(Horse, Donkey):
    """骡子类"""
    pass

mule = Mule()
mule.run()
mule.walk()