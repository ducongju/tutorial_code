# 类名按照大驼峰命名法
class Game(object):
    top_score = 0  # 类属性名

    def __init__(self, player_name):  # __init__方法: 使用类名()创建对象的时候，会自动调用初始化方法
        self.player_name = player_name  # 实例属性名
        self.__age = 18  # 私有属性名: 在外界不能够被直接访问

    @classmethod
    def show_top_score(cls):  # 类方法名
        print("历史记录 %d" % cls.top_score)

    @staticmethod
    def show_help():  # 静态方法名
        print("帮助信息：让僵尸进入大门")

    def start_game(self):  # 实例方法名
        print("%s 开始游戏啦..." % self.player_name)

    def __secret(self):  # 私有方法名: 不允许在外界直接访问
        print("%s 的年龄是 %d" % (self.player_name, self.__age))

    def __str__(self):  # __str__方法: 必须返回一个字符串
        return "我叫[%s]" % self.player_name

    def __del__(self):  # __del__方法: del关键字可以删除一个对象
        print("%s 我去了" % self.player_name)

    def __call__(self, player_name2):  # __call__方法
        self.player_name2 = player_name2
        return self


# 查看游戏的帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建游戏对象
game = Game("小明")

# 返回字符串信息
print(game)

# 游戏开始了
game.start_game()

# 创建新的游戏对象
game2 = game("小红")

# 删除游戏对象
del game
