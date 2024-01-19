import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def knn_classifier(records, k, query_point):
    distances = [(euclidean_distance(query_point, record[:2]), record[2]) for record in records]
    distances.sort()  # Sort by distance
    k_nearest_neighbors = distances[:k]
    average_y = round(sum(neighbor[1] for neighbor in k_nearest_neighbors) / k)
    return int(average_y)  # Assuming Y is a whole number

def main():
    # Input: User-specified number of records
    num_records = int(input("Enter the number of records: "))
    records = []
    for _ in range(num_records):
        record = tuple(map(float, input("Enter record (x1, x2, Y): ").split()))
        records.append(record)

    # Input: Value of k
    k = int(input("Enter the value of k: "))

    # Input: (x, y) for query point
    query_point = tuple(map(float, input("Enter the query point (x, y): ").split()))

    # Perform KNN classification
    result = knn_classifier(records, k, query_point)

    # Output
    print(f"The predicted Y value for the query point is: {result}")

if __name__ == "__main__":
    main()
