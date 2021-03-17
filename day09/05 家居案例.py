class HouseItem:
    """家具类"""
    def __init__(self, name, area):
        """初始化方法"""
        self.name = name
        self.area = area

    def __str__(self):
        """打印家具对象的描述信息"""
        return "家具名字：%s   占地面积：%.1f平方米" % (self.name, self.area)

bed = HouseItem("席梦思", 4)
print(bed)

chest = HouseItem("衣柜", 2)
print(chest)

table = HouseItem("餐桌", 1.5)
print(table)


class House:
    """房子类"""
    def __init__(self, house_type, area):
        """初始化方法"""
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        """打印房子的信息"""
        return "户型为：%s  总面积为：%.1f㎡  剩余面积为：%.1f㎡  家具名称列表为：%s" % \
               (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        """添加家具的方法"""
        # 1.判断房子的剩余面积和家具的面积大小
        #   如果房子的剩余面积小于家具的面积，不能添加，给个提示信息，代码不再向下执行
        if self.free_area < item.area:
            print("添加%s家具的面积太大，无法添加。" % item.name)
            return
        #   如果房子的剩余面积不下于家具的面积，可以添加家具
        # 2.更新房子的剩余面积
        self.free_area -= item.area
        # 3.把新添加的家具名称保存到家具名称列表
        self.item_list.append(item.name)

house = House("别墅", 200)
# print(house)
house.add_item(bed)
print(house)
house.add_item(chest)
print(house)
house.add_item(table)
print(house)
