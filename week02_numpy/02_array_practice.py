import numpy as np

def main():
    matrix = np.array([
        [10,20,30,40],
        [50,60,70,80],
        [90,100,110,120],
        [130,140,150,160]
    ])

    print(matrix)
    print(matrix.shape)
    print(matrix.dtype)
    print(matrix[0,:])
    print(matrix[:,2])
    print(matrix[3,1])
    print(matrix[2:4,2:4])
    print(matrix * 2)

if __name__ == "__main__":
    main()