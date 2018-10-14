import os.path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.advanced_activations import LeakyReLU
from keras.optimizers import SGD


if __name__ == "__main__":
    # 读取数据
    input = pd.read_csv("./input.txt", sep='\t', header=None)
    output = pd.read_csv("./output.txt", sep='\t', header=None)
    # 预处理数据
    # 分割数据
    x_train, x_test, y_train, y_test = train_test_split(input, output, test_size=0.2)
    # 标准化数据
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train)
    y_test = std_y.transform(y_test)
    # print(x_train)
    # print(y_train)
    # 模型
    model = Sequential()
    # 一层1024个神经元
    model.add(Dense(1024, input_dim=5))
    # model.add(LeakyReLU(alpha=0.1))
    # sigmoid激活函数
    model.add(Activation("sigmoid"))
    model.add(Dense(1024))
    # model.add(LeakyReLU(alpha=0.1))
    model.add(Activation("sigmoid"))
    model.add(Dense(1024))
    # model.add(Activation("relu"))
    # model.add(Dense(16))
    # model.add(LeakyReLU(alpha=0.1))
    model.add(Activation("sigmoid"))
    model.add(Dense(6))
    # model.add(Activation("softmax"))

    # 求解
    # 计算mean_squared_error
    model.compile(loss="mse", optimizer=SGD(lr=0.003))
    
    # 加载权重
    if os.path.exists('001.h5'):
        model.load_weights('001.h5')

    # 跑10000次
    model.fit(x_train, y_train, epochs=200000)

    # 保存结果
    model.save_weights('001.h5')
    # 输出
    # 预测结果
    y_predict = model.predict(x_test)
    # 反标准化
    y_predict = std_y.inverse_transform(y_predict)
    print(std_y.inverse_transform(y_test))
    print(y_predict)
    # 评估结果
    score = model.evaluate(x_test, y_test)
    print(score)
