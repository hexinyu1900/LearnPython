class Gun:
    """枪支类"""
    def __init__(self, type):
        """初始化方法"""
        self.type = type
        self.bullet_count = 0

    def add_bullet(self, count):
       """添加子弹方法"""
       self.bullet_count += count
    def shoot(self):
       """射击方法"""
       if self.bullet_count <= 0:
           print("没有子弹不能射击，请先添加子弹。")
           return
       self.bullet_count -= 1
       print("剩余子弹数量：%d" % self.bullet_count)

# ak47 = Gun("AK47")
# ak47.add_bullet(50)
# ak47.shoot()

class Soldier:
    """士兵类"""
    def __init__(self, name, gun = None):
        """初始化方法"""
        self.name = name
        self.gun = gun

    def add(self, new_count):
        """士兵拿着枪添加子弹"""
        # 1.判断士兵有没有枪，如果没有枪，不能开火，提示分配枪支
        if self.gun == None:
            print("当前士兵%s没有枪，不能开火，请分配枪支" % self.name)
            return
        # 2.如果士兵有枪，士兵要拿着枪去添加子弹
        self.gun.add_bullet(new_count)

    def fire(self):
        """开火的方法"""
        # 1.判断士兵有没有枪，如果没有枪，不能开火，提示分配枪支
        if self.gun == None:
           print("当前士兵%s没有枪，不能开火，请分配枪支" % self.name)
           return
        # 3.如果士兵有枪，士兵要拿着枪去射击
        self.gun.shoot()

ak74 = Gun("ak47")
tom = Soldier("许三多", ak74)
tom.add(50)
tom.fire()
tom.fire()
