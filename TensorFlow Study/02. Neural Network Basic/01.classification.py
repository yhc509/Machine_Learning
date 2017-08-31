#-*- coding: utf-8 -*-
# 털과 날개가 있는지 없는지에 따라, 포유류인지 조류인지 분류하는 신경망 모델을 만들어봅니다.
# 입력 데이터는 Hot-encording 을 이용

import tensorflow as tf
import numpy as np

# [털, 날개]
x_data = np.array(
    [[0, 0], [1, 0], [1, 1], [0, 0], [0, 0], [0, 1]])

# [기타, 포유류, 조류]
# 다음과 같은 형식을 one-hot 형식의 데이터라고 합니다.
y_data = np.array([
    [1, 0, 0],  # 기타
    [0, 1, 0],  # 포유류
    [0, 0, 1],  # 조류
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 1]
])

################
# 신경망 모델 구성 #
################
X = tf.placeholder(tf.float32,name="X")
Y = tf.placeholder(tf.float32,name="Y")

# 첫번째 가중치의 차원은 2차원으로 [특성, 히든 레이어의 뉴런갯수] -> [2, 10] 으로 정합니다.
W1 = tf.Variable(tf.random_uniform([2, 10], -1., 1.),name="W1")
# 두번째 가중치의 차원을 [첫번째 히든 레이어의 뉴런 갯수, 분류 갯수] -> [10, 3] 으로 정합니다.
W2 = tf.Variable(tf.random_uniform([10, 3], -1., 1.),name="W2")

# 편향을 각각 각 레이어의 아웃풋 갯수로 설정합니다.
# b1 은 히든 레이어의 뉴런 갯수로, b2 는 최종 결과값 즉, 분류 갯수인 3으로 설정합니다.
b1 = tf.Variable(tf.zeros([10]),name="b1")
b2 = tf.Variable(tf.zeros([3]),name="b2")

# 신경망의 히든 레이어에 가중치 W1과 편향 b1을 적용합니다
L = tf.add(tf.matmul(X, W1), b1)
# 가중치와 편향을 이용해 계산한 결과 값에
# 텐서플로우에서 기본적으로 제공하는 활성화 함수인 ReLU 함수를 적용합니다.
L = tf.nn.relu(L)ㄴ
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)ㄴ

for step in xrange(100):
    sess.run(train_op, feed_dict={X: x_data, Y: y_data})

    if (step + 1) % 10 == 0:
        print (step + 1), sess.run(cost, feed_dict={X: x_data, Y: y_data})


##########################
# 결과 확인				 #
# 0: 기타 1: 포유류, 2: 조류 #
##########################

# tf.argmax: 예측값과 실제값의 행렬에서 tf.argmax 를 이용해 가장 큰 값을 가져옵니다.
# 예) [[0 1 0] [1 0 0]] -> [2 1]
#    [[0.2 0.7 0.1] [0.9 0.1 0.]] -> [2 1]
prediction = tf.argmax(model, 1)
target = tf.argmax(Y, 1)
print ('예측값:', sess.run(prediction, feed_dict={X: x_data}))
print ('실제값:', sess.run(target, feed_dict={Y: y_data}))

check_prediction = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(check_prediction, tf.float32))
print ('정확도: %.2f' % sess.run(accuracy * 100, feed_dict={X: x_data, Y: y_data}))