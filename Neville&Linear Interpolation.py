import math
import datetime as dt
# part 4
# Question number 32 - interpolation methods
import math


# part 4
# Question number 32 - interpolation methods
def linear_interpolation(points_table, point):
    x1 = math.ceil(point)  # if point is for example = 0.65, its will up the number to 1
    x2 = x1 - 1  # then we find the number who is smallwer than 0.65 (0)
    y1 = points_table[x1][1]  # brings the y from the table
    y2 = points_table[x2][1]
    return ((y1 - y2) / (x1 - x2)) * point + (y2 * x1) - (y1 * x2) / (x1 - x2)


def Neville_interpolation(points_table, point):
    i=0
    j=0
    for j in range(1, len(points_table)):
        for i in range(len(points_table) - 1, j - 1, -1):
            if points_table[i][0] - points_table[i - j][0] == 0:
                continue
            else:
                points_table[i][1] = ((point - points_table[i - j][0]) * points_table[i][1] - (
                        point - points_table[i][0]) * points_table[i - 1][1]) / (
                                                 points_table[i][0] - points_table[i - j][0])
                print("[", i, ",", j, "]=", round(points_table[i][1], 5))
    sum = points_table[len(points_table) - 1][1]
    return sum


def EndOfCal(end):
    i = 0
    if end < 0:
        i = 1
        end = abs(end)
    day = (format(dt.datetime.today().day))
    hour = (format(dt.datetime.today().hour))
    minute = (format(dt.datetime.today().minute))
    temp = 1 / 100000
    end = str(end) + "00000"
    print(str(end)+day+hour+minute)


def main():
    point = 0.65
    points_table = [[0.2, 13.7241], [0.35, 13.9776], [0.45, 14.0625], [0.6, 13.9776], [0.75, 13.7241], [0.85, 13.3056],
                    [0.9, 12.7281]]
    sum = linear_interpolation(points_table, point)
    print("Linear Interpolation: f(x)=",sum)
    EndOfCal(round(sum, 3))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Neville Interpolation:")
    sum = Neville_interpolation(points_table, point)
    print("Final result: f(x)=")
    EndOfCal(round(sum,3))


if __name__ == "__main__":
    main()
