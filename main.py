import csv
import math
import operator

def data_process():
    return 0

def get_iris_prediction(list_K_neighbors):
    prediction_vote = {}

    for i in range(len(list_K_neighbors)):
        if list_K_neighbors[i][0][4] in prediction_vote:    #list_K_neighbors[i][0][4] is the category of iris
            prediction_vote[list_K_neighbors[i][0][4]] += 1

        else:    
            prediction_vote[list_K_neighbors[i][0][4]] = 0
            prediction_vote[list_K_neighbors[i][0][4]] += 1

    sort_prediction_vote = sorted(prediction_vote.items(), key=operator.itemgetter(1), reverse=True)
    #if two class got same vote, return both as list
    #sort_prediction_vote{class,vote}
    try:        
        if sort_prediction_vote[0][1] == sort_prediction_vote[1][1]:
            prediction = []
            prediction.append(sort_prediction_vote[0][0])
            prediction.append(sort_prediction_vote[1][0])
            return  prediction
    except:
        prediction = []
        prediction.append(sort_prediction_vote[0][0])

    prediction = []     #no error if there is two or more class in sort_prediction_vote
    prediction.append(sort_prediction_vote[0][0])

    return prediction

def get_euclidean_distance(test_datapoint, train_datapoint): # use Euclidean distance formula
    #sqrt((q1-p1)^2+(q2-p2)^2+...+(qn-pn)^2)
    euclidean_distance = 0
    inner_inner_value = 0.0
    inner_value = 0.0

    for i in range(4):
        inner_inner_value = float(test_datapoint[i]) - float(train_datapoint[i]) 
        inner_value += inner_inner_value**2
    euclidean_distance = math.sqrt(inner_value)

    return euclidean_distance

def get_K_neighbors(test_datapoint, list_train_data, K):
    list_distance = []      #hold all distance

    for i in range(len(list_train_data)):
        distance = get_euclidean_distance(test_datapoint, list_train_data[i])
        list_distance.append((list_train_data[i], distance))

    list_distance.sort(key=operator.itemgetter(1))       #sort all distance in the list
    print(list_distance)
    
    list_K_neighbors = []
    for i in range(K):
        list_K_neighbors.append(list_distance[i])

    return list_K_neighbors #return K number of K neighbors

def result():
    #prepare data
    with open('shuffled_bezdekIris_80_percent_data.csv', newline='') as f:
        reader = csv.reader(f)
        list_train_data = list(reader)

    test_datapoint = input('Enter value in format: length_sepal,width_sepal,length_petal,width_petal')  
    test_datapoint = test_datapoint.split(",")

    for i in range(len(test_datapoint)):
        test_datapoint[i] = float(test_datapoint[i]) 

    #evulate data
    K = 5
    list_K_neighbors = get_K_neighbors(test_datapoint, list_train_data, K)
    print_list_K_neighbors = []

    #transfer list_K_neighbors into easy read list print_list_K_neighbors and print it
    for i in range(len(list_K_neighbors)):
        print_list_K_neighbors.append(list_K_neighbors[i][0][4])
    print('K_neighbors: ' + str(print_list_K_neighbors) )

    iris_prediction = get_iris_prediction(list_K_neighbors)     #return as list as maybe two potential class

    #print result according to two condition
    if len(iris_prediction) == 2:
        print('Prediction: '+ iris_prediction[0] +' or '+ iris_prediction[1])
    else:
        print('Prediction:', iris_prediction[0])


################################
if __name__ == "__main__":
    result()