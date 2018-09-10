import tensorflow as tf
x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1,x2)
# defines our session and launches graph
sess = tf.Session()
# runs result
print(sess.run(result))
sess.close()


##GPU version 설치시에만 사용 가
with tf.Session() as sess:
  with tf.device("/gpu:1"):
    matrix1 = tf.constant([[3., 3.]])
    matrix2 = tf.constant([[2.],[2.]])
    product = tf.matmul(matrix1, matrix2)
