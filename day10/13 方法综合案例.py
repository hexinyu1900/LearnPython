class Game:
    """Game类"""
    # 类属性
    top_score = 0

    def __init__(self,player_name):
        """初始化方法"""
        self.player_name = player_name

    def start_game(self):
        """实例方法"""
        print("开始玩家%s的游戏" % self.player_name)
        Game.top_score += 100

    @classmethod
    def show_top_socre(cls):
        """类方法"""
        print("历史最高分为%d" % cls.top_score)

    @staticmethod
    def show_help():
        """静态方法"""
        print("显示帮助信息")


Game.show_help()
Game.show_top_socre()
rdj = Game("RDJ")
rdj.start_game()
Game.show_top_socre()



