#要是用多个二分类模型如logsitic则label数据集是一个矩阵，某一列非0即1的二分类数据
#若直接是多分类模型，如softmax,则label只需为一列即可,多此时非此即彼，即所有类求和为1
from sklearn.cross_validation import train_test_split
from sklearn.svm import LinearSVC#模型训练时是一对多one-vs-rest classifiers，并非使用softmax
from sklearn.ensemble import GradientBoostingClassifier
# X_train,X_val，y_train, y_val=train_test_split()