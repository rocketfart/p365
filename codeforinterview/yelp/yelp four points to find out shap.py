# coding=utf-8
def findshap(self):
    points = [[0,0], [2,1], [3,-1], [1, -2]]
    # 平行四边形 都是是对角相切相等 找到中点做计算 两队 垂直，相等正方形，垂直不相等 菱形，不垂直 相等 菱形，不垂直不相等长方
    for i in points:
        i[0],i[1]=float(i[0]),float(i[1])
    mid = [sum(i[0] / 4.0 for i in points), sum(i[1] / 4.0 for i in points)]

    v1 = [points[0][0] - mid[0],points[0][1]-mid[1]]
    f1 = [mid[0] - v1[0],mid[1]-v1[1]]
    if f1 not in points: return -1

    group1 = [points[0], f1]

    group2 = points
    group2.remove(f1)
    group2.remove(points[0])

    slop1 = (group1[1][1] - group1[0][1]) / (group1[1][0] - group1[0][0]) if (group1[1][0] - group1[0][0]) else 1
    slop2= (group2[1][1] - group2[0][1]) / (group2[1][0] - group2[0][0]) if (group2[1][0] - group2[0][0]) else 1


    lenslop1 = (group1[1][1] - group1[0][1]) ** 2 + (group1[1][0] - group1[0][0]) ** 2
    lenslop2 = (group2[1][1] - group2[0][1]) ** 2 + (group2[1][0] - group2[0][0]) ** 2

    if slop1 * slop2 == 1 or [slop1, slop2] in [1, 0] or [0, 1]:
        if lenslop1 == lenslop2:
            return 'square'
        else:
            return 'rectangle'
    else:
        if lenslop1 == lenslop2:
            return 'diamond'
        else:
            return 'parallergram'


if __name__ == '__main__':
    print findshap(1)
