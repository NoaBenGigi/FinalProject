import datetime as dt
def EndOfCal(end):
    i=0
    if end<0:
        i=1
        end=abs(end)
    day=(format(dt.datetime.today().day))
    hour=(format(dt.datetime.today().hour))
    minute=(format(dt.datetime.today().minute))
    temp=1/100000
    help=temp*(1/100*(float(day)+1/100*float(hour)+1/10000*float(minute))*1/1000)
    end+=help
    print("End calucate With Date-->")
    if i==1:
        print("-"+end.__str__())
    if i==0:
        print(end)

def print_matrix(A):
    """this func print that matrix
    :param A: matrix
    :return: no return value
    """
    print('\n'.join(['\t'.join(['{:4}'.format(item) for item in row])
                     for row in A]))


def copy_matrix(mat):
    """
    :param mat: matrix
    :return: deep copy of matrix
    """
    copy_mat = [[0] * len(mat[0]) for _ in range(len(mat))]  # creating new zero matrix
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            copy_mat[i][j] = mat[i][j]
    return copy_mat


def gauss_zaidel(mat, b):
    print("~~~Gauss~~~")
    number_of_iteration = 1
    epsilon = 0.00001
    print("epsilon= ", epsilon)
    x, y, z = 0, 0, 0
    x_r1 = (b[0][0] - mat[0][1] * y - mat[0][2] * z) / mat[0][0]
    y_r1 = (b[1][0] - mat[1][0] * x_r1 - mat[1][2] * z) / mat[1][1]
    z_r1 = (b[2][0] - mat[2][0] * x_r1 - mat[2][1] * y_r1) / mat[2][2]
    print("Iteration number:\t", number_of_iteration, "\tXr+1 Value:\t", x_r1, "\tYr+1 Value:\t", y_r1,
          "\tZr+1 Value:\t", z_r1)
    while abs(x_r1 - x) > epsilon:
        x = x_r1
        y = y_r1
        z = z_r1
        x_r1 = (b[0][0] - mat[0][1] * y - mat[0][2] * z) / mat[0][0]
        y_r1 = (b[1][0] - mat[1][0] * x - mat[1][2] * z) / mat[1][1]
        z_r1 = (b[2][0] - mat[2][0] * x - mat[2][1] * y) / mat[2][2]
        number_of_iteration += 1
        print("Iteration number:\t", number_of_iteration, "\tXr+1 Value:\t", x_r1, "\tYr+1 Value:\t", y_r1,
              "\tZr+1 Value:\t", z_r1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    EndOfCal(-2)
    EndOfCal(1.5)
    EndOfCal(1)
    print("Total of iterations:\t", number_of_iteration)


def main():
    A = [[10, 8, 1],
         [4, 10, -5],
         [5,1, 10]]

    b = [[-7], [2], [1.5]]

    print_matrix(A)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Gauss-Zaidel Method")
    gauss_zaidel(A, b)



if __name__ == "__main__":
    main()
