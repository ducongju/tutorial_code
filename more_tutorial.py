import json
from pprint import pprint

try:
    import cPickle as pickle
except:
    import pickle

choose = 3

# pickle, cPickle 模块：序列化 Python 对象
if choose == 1:
    """pickle 模块实现了一种算法，可以将任意一个 Python 对象转化为一系列的字节，也可以将这些字节重构为一个有相同特征的新对象。
    由于字节可以被传输或者存储，因此 pickle 事实上实现了传递或者保存 Python 对象的功能。
    cPickle 使用 C 而不是 Python 实现了相同的算法，因此速度上要比 pickle 快一些。但是它不允许用户从 pickle 派生子类。
    如果子类对你的使用来说无关紧要，那么 cPickle 是个更好的选择。"""
    data = [{'a': 'A', 'b': 2, 'c': 3.0}]
    data_string = pickle.dumps(data)
    data_from_string = pickle.loads(data_string)

    # 将对象存入文件
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)

    # 从文件中读取
    with open("data.pkl","rb") as f:
        data_from_file = pickle.load(f)
        print(data_from_file)

# pprint 模块：打印 Python 对象
elif choose == 2:
    """pprint 是 pretty printer 的缩写，用来打印 Python 数据结构，与 print 相比，它打印出来的结构更加整齐，便于阅读。"""
    data = (
        "this is a string",
        [1, 2, 3, 4],
        ("more tuples", 1.0, 2.3, 4.5),
        "this is yet another string"
    )
    print(data)
    pprint(data)


# json 模块：处理 JSON 数据
elif choose == 3:
    """JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写，同时也易于机器解析和生成。"""
    # 将 JSON 对象写入了一个字符串
    info_string = """
    {
        "name": "echo",
        "age": 24,
        "coding skills": ["python", "matlab", "java", "c", "c++", "ruby", "scala"],
        "ages for school": { 
            "primary school": 6,
            "middle school": 9,
            "high school": 15,
            "university": 18
        },
        "hobby": ["sports", "reading"],
        "married": false
    }
    """

    # 用 json.loads() (load string) 方法从字符串中读取 JSON 数据
    # 此时，我们将原来的 JSON 数据变成了一个 Python 对象，在我们的例子中这个对象是个字典（也可能是别的类型，比如列表）
    info = json.loads(info_string)
    # pprint(info_string)
    # pprint(info)
    # print(type(info))

    # 使用 json.dumps() 将一个 Python 对象变成 JSON 对象
    info_json = json.dumps(info)
    # pprint(info_json)

    # 与 pickle 类似，我们可以直接从文件中读取 JSON 数据，也可以将对象保存为 JSON 格式
    # 将对象保存为 JSON 格式的文件
    with open("info.json","w") as f:
        json.dump(info, f)

    # 从 JSON 文件中读取数据
    with open("info.json") as f:
        pprint(json.load(f))
