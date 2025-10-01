#随机数字典key：1-100，value随机
import random
import pprint

values=random.sample(range(1,10001),100)

my_dict={f"key{i+1}":values[i] for i in range(100)}

pprint.pprint(my_dict)