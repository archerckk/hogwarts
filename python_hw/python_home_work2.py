import yaml


class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        '这是叫方法'
        print('正在叫')

    def run(self):
        '这是跑方法'
        print('正在跑')


class Cat(Animal):

    def __init__(self, name="Tom", color='Bule', age='5', gender='Man', hair='短毛'):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def catch_mouse(self):
        '抓老鼠方法'
        print('正在捉老鼠')

    def call(self):
        '重写父类方法'
        print('正在喵喵叫')


class Dog(Animal):

    def __init__(self, name="Peter", color='Bule', age='5', gender='Man', hair='长毛'):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def watch_home(self):
        '会看家方法'
        print('正在看家')

    def call(self):
        '重写父类方法'
        print('正在汪汪叫')


with open('class_attribute.yml', encoding='UTF-8')as f:
    datas = yaml.safe_load(f)

print(datas["dog"][0]['dog1'])

cat = Cat(datas['cat'][0]['cat1']['name'], datas['cat'][0]['cat1']['color']
          , datas['cat'][0]['cat1']['age'], datas['cat'][0]['cat1']['gender'])
# 调用抓猫鼠方法
cat.catch_mouse()
# 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
print(f'猫猫名:{cat.name},颜色：{cat.color}，性别：{cat.gender},毛发：{cat.hair}，抓到老鼠了')

dog = Dog(datas['dog'][0]['dog1']['name'], datas['dog'][0]['dog1']['color']
          , datas['dog'][0]['dog1']['age'], datas['dog'][0]['dog1']['gender'])

# 调用【会看家】的方法
dog.watch_home()

# 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
print(f'狗狗名:{dog.name},颜色：{dog.color}，性别：{dog.gender},毛发：{dog.hair}')
