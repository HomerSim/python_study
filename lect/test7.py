#모듈 
# from 안쓰면 module. 이렇게 해야함 from 쓰면 module 안붙여도됨
import module

#from module import MarketGoods, add


fish1 = module.MarketGoods(size=20, price=500)
fish1.show()

print(module.add(3,5))