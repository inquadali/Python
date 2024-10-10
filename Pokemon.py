# 宠物小精灵对战游戏
# 这是一个练习Python基础知识的小项目
# 知识点: 类、列表、字典、循环、条件判断、函数等

class Pokemon:
    def __init__(self, name, hp, attack, defense):
        self.name = name            # 精灵名称
        self.hp = hp               # 生命值
        self.attack = attack       # 攻击力
        self.defense = defense     # 防御力
        self.skills = []           # 技能列表

    def learn_skill(self, skill_name, damage):
        """学习新技能"""
        if len(self.skills) < 4:    # 最多学习4个技能
            self.skills.append({"name": skill_name, "damage": damage})
            print(f"{self.name}学会了{skill_name}!")
        else:
            print("技能已达到上限!")

    def show_skills(self):
        """显示所有技能"""
        print(f"\n{self.name}的技能列表:")
        for i, skill in enumerate(self.skills, 1):
            print(f"{i}. {skill['name']} - 威力: {skill['damage']}")

    def attack_opponent(self, opponent, skill_index):
        """攻击对手"""
        if 0 <= skill_index < len(self.skills):
            skill = self.skills[skill_index]
            damage = (self.attack + skill["damage"]) - opponent.defense
            if damage < 0:
                damage = 0
            opponent.hp -= damage
            print(f"{self.name}使用了{skill['name']}, 对{opponent.name}造成了{damage}点伤害!")
            print(f"{opponent.name}剩余生命值: {opponent.hp}")
        else:
            print("无效的技能选择!")

# ===== 练习任务 =====
# 1. 创建两个宠物小精灵
pikachu = Pokemon("皮卡丘", hp=100, attack=50, defense=30)
charmander = Pokemon("小火龙", hp=110, attack=45, defense=35)

# 2. 让精灵学习技能
# 请为皮卡丘添加3个技能
pikachu.learn_skill("电击", 40)
# TODO: 添加更多技能...

# 3. 为小火龙添加技能
# TODO: 为小火龙添加技能...

# 4. 展示双方技能
pikachu.show_skills()
charmander.show_skills()

# 5. 进行对战
# TODO: 编写一个对战循环，直到一方生命值降为0
# 提示：使用while循环，让双方轮流攻击

"""
扩展练习：
1. 添加更多属性（如：速度、暴击率等）
2. 实现技能特殊效果（如：麻痹、烧伤等）
3. 添加对战时的随机因素
4. 创建更多种类的精灵
"""
