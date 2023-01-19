import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

from sklearn.metrics import confusion_matrix


zararsizlar_df = pd.read_csv("C:\\Users\\muham\\GITHUB_REPOLAR\\PhisDetection\\yapilandirilmis_zararsiz_site_verileri.csv")
phishing_siteler_df = pd.read_csv("C:\\Users\muham\\GITHUB_REPOLAR\\PhisDetection\\yapilandirilmis_phishing_site_verileri.csv")


df = pd.concat([zararsizlar_df, phishing_siteler_df], axis=0)
df = df.sample(frac=1)

df = df.drop('url', axis=1)
df = df.drop('baslik_kontrol', axis=1)
df = df.drop_duplicates()
#df = df.replace([np.inf, -np.inf], 0)
X = df.drop("label", axis=1)
Y = df["label"]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=10)
#x_train[np.isinf(x_train)] = np.finfo(x_train.values.dtype).max
#x_test[np.isinf(x_test)] = np.finfo(x_test.values.dtype).max
#x_train = imputer.fit_transform(x_train)
#x_test = imputer.fit_transform(x_test)
#y_train = imputer.fit_transform(y_train)
#y_test = imputer.fit_transform(y_test)

svm_model = svm.LinearSVC()

rf_model = RandomForestClassifier(n_estimators=60)

dt_model = tree.DecisionTreeClassifier()

ab_model = AdaBoostClassifier()

nb_model = GaussianNB()


#tahminler = svm_model.predict(x_test)


#tn, tp, fn, fp = confusion_matrix(y_true=y_test, y_pred=tahminler).ravel()


#dogruluk_accurucy = (tp + tn) / (tp + tn + fp + fn)

#presicion = tp / (tp + fp)

#recall = tp / (tp + fn)

#print("dogruluk_accurucy ===> ", dogruluk_accurucy, "\n"
#      "presicion ====> ", presicion, "\n"
#      "recall ====>", recall )


K = 5

total = X.shape[0]
index = int(total / K)

# FAZ 1

X_1_test = X.iloc[:index]
X_1_train = X.iloc[index:]
Y_1_test = Y.iloc[:index]
Y_1_train = Y.iloc[index:]


# FAZ 2

X_2_test = X.iloc[index:index*2]
X_2_train = X.iloc[np.r_[:index, index*2:]]
Y_2_test = Y.iloc[index:index*2]
Y_2_train = Y.iloc[np.r_[:index, index*2:]]

# FAZ 3

X_3_test = X.iloc[index*2:index*3]
X_3_train = X.iloc[np.r_[:index*2, index*3:]]
Y_3_test = Y.iloc[index*2:index*3]
Y_3_train = Y.iloc[np.r_[:index*2, index*3:]]

# FAZ 4

X_4_test = X.iloc[index*3:index*4]
X_4_train = X.iloc[np.r_[:index*3, index*4:]]
Y_4_test = Y.iloc[index*3:index*4]
Y_4_train = Y.iloc[np.r_[:index*3, index*4:]]

# FAZ 5

X_5_test = X.iloc[index*4:]
X_5_train = X.iloc[:index*4]
Y_5_test = Y.iloc[index*4:]
Y_5_train = Y.iloc[:index*4]


X_train_list = [X_1_train, X_2_train, X_3_train, X_4_train, X_5_train]
X_test_list = [X_1_test, X_2_test, X_3_test, X_4_test, X_5_test]

Y_train_list = [Y_1_train, Y_2_train, Y_3_train, Y_4_train, Y_5_train]
Y_test_list = [Y_1_test, Y_2_test, Y_3_test, Y_4_test, Y_5_test]


def hesaplamalar(TN, TP, FN, FP):
      model_accuricy_dogruluk = (TP + TN) / (TP + TN + FN + FP)
      model_presicion = TP / (TP + FP)
      model_recall = TP / (TP + FN)
      return model_accuricy_dogruluk, model_presicion, model_recall


rf_accuracy_list, rf_persicion_list, rf_recall_list = [], [], []
dt_accuracy_list, dt_persicion_list, dt_recall_list = [], [], []
ab_accuracy_list, ab_persicion_list, ab_recall_list = [], [], []
svm_accuracy_list, svm_persicion_list, svm_recall_list = [], [], []
nb_accuracy_list, nb_persicion_list, nb_recall_list = [], [], []


for i in range(0, K):
      #RANDOM FOREST EĞİTİMİ
      rf_model.fit(X_train_list[i],Y_train_list[i])
      rf_predictions = rf_model.predict(X_test_list[i])
      tn, tp , fn, fp = confusion_matrix(y_true=Y_test_list[i], y_pred=rf_predictions).ravel()
      rf_accuracy, rf_presicion, rf_recall = hesaplamalar(tn, tp, fn, fp)
      rf_accuracy_list.append(rf_accuracy)
      rf_persicion_list.append(rf_presicion)
      rf_recall_list.append(rf_recall)


      #KARAR AĞACI EĞİTİMİ
      dt_model.fit(X_train_list[i],Y_train_list[i])
      dt_predictions = dt_model.predict(X_test_list[i])
      tn, tp , fn, fp = confusion_matrix(y_true=Y_test_list[i], y_pred=dt_predictions).ravel()
      dt_accuracy, dt_presicion, dt_recall = hesaplamalar(tn, tp, fn, fp)
      dt_accuracy_list.append(dt_accuracy)
      dt_persicion_list.append(dt_presicion)
      dt_recall_list.append(dt_recall)

      #DESTEK VEKTÖR MAKİNASI EĞİTİMİ
      svm_model.fit(X_train_list[i],Y_train_list[i])
      svm_predictions = svm_model.predict(X_test_list[i])
      tn, tp , fn, fp = confusion_matrix(y_true=Y_test_list[i], y_pred=svm_predictions).ravel()
      svm_accuracy, svm_presicion, svm_recall = hesaplamalar(tn, tp, fn, fp)
      svm_accuracy_list.append(svm_accuracy)
      svm_persicion_list.append(svm_presicion)
      svm_recall_list.append(svm_recall)

      #ADA BOOST EĞİTİMİ
      ab_model.fit(X_train_list[i],Y_train_list[i])
      ab_predictions = ab_model.predict(X_test_list[i])
      tn, tp , fn, fp = confusion_matrix(y_true=Y_test_list[i], y_pred=ab_predictions).ravel()
      ab_accuracy, ab_presicion, ab_recall = hesaplamalar(tn, tp, fn, fp)
      ab_accuracy_list.append(ab_accuracy)
      ab_persicion_list.append(ab_presicion)
      ab_recall_list.append(ab_recall)

      #GAUSSİAN EĞİTİMİ
      nb_model.fit(X_train_list[i], Y_train_list[i])
      nb_predictions = nb_model.predict(X_test_list[i])
      tn, tp , fn, fp = confusion_matrix(y_true=Y_test_list[i], y_pred=nb_predictions).ravel()
      nb_accuracy, nb_presicion, nb_recall = hesaplamalar(tn, tp, fn, fp)
      nb_accuracy_list.append(nb_accuracy)
      nb_persicion_list.append(nb_presicion)
      nb_recall_list.append(nb_recall)



RF_accuracy = sum(rf_accuracy_list) / len(rf_accuracy_list)
RF_presicion = sum(rf_persicion_list) / len(rf_persicion_list)
RF_recall = sum(rf_recall_list) / len(rf_recall_list)
print("RF_accuracy : ", RF_accuracy, " \n RF_presicion : ", RF_presicion, "\n RF_recall :  ", RF_recall)

DT_accuracy = sum(dt_accuracy_list) / len(dt_accuracy_list)
DT_presicion = sum(dt_persicion_list) / len(dt_persicion_list)
DT_recall = sum(dt_recall_list) / len(dt_recall_list)
print("DT_accuracy : ", DT_accuracy, "\n DT_presicion :  ", DT_presicion, "\n DT_recall :  ", DT_recall)

SVM_accuracy = sum(rf_accuracy_list) / len(rf_accuracy_list)
SVM_presicion = sum(rf_persicion_list) / len(rf_persicion_list)
SVM_recall = sum(rf_recall_list) / len(rf_recall_list)
print("SVM_accuracy :  ", SVM_accuracy, " \nSVM_presicion : ", SVM_presicion, "\nSVM_recall : ", SVM_recall)

NB_accuracy = sum(nb_accuracy_list) / len(nb_accuracy_list)
NB_presicion = sum(nb_persicion_list) / len(nb_persicion_list)
NB_recall = sum(nb_recall_list) / len(nb_recall_list)
print("NB_accuracy : ", NB_accuracy, "\n NB_presicion : ", NB_presicion, " \nNB_recall : ", NB_recall)

AB_accuracy = sum(ab_accuracy_list) / len(ab_accuracy_list)
AB_presicion = sum(ab_persicion_list) / len(ab_persicion_list)
AB_recall = sum(ab_recall_list) / len(ab_recall_list)
print("AB_accuracy : ", AB_accuracy, "\nAB_presicion : ", AB_presicion, "\nAB_recall : ", AB_recall)
