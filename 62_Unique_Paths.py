# day 21 2019-05-30 Thu
# 62. Unique Paths
# DP method
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[0]*m]*n
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    mem[i][j] = 1
                elif i == n-1:
                    mem[i][j] = mem[i][j+1]
                elif j == m-1:
                    mem[i][j] = mem[i+1][j]
                else:
                    mem[i][j] = mem[i+1][j] + mem[i][j+1]
        return mem[0][0]

"""
https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-to-be-a-better-man-3-2/ 
"""
思路： 【1】考虑位置X,Y。到达该位置一共有2条线路，从上面的格子过来或从左边的格子过来。不可能从下面的格子和右边的格子过来。 【2】所以path【x,y】=path【x-1,y】+path【x,y-1】 【3】​​​注意考虑特殊情况，边缘位置，当x等于1时，只能从上面过来，不可能从左边过来。当y等于 1时，只能从左边过来。 【4】但是这样会出现重复计算，超出时间限制。例如【5，3】和【4，4】都要计算到达【4，3】位置的步数，一个是从左边来的格子，一个从上面来的格子。这样就出现了重复计算。 【5】解决方法：采用一个m*n的二维数组来存储到达当前格子的步数，初始化时将二维数组中的所有数置为0，当遍历到该位置时，记录下当前位置个步数。

int** res;    
//动态规划到达X,y所拥有的路径
int dpPath(int x, int y) {
	if (res[x - 1][y - 1] != 0) {
		return res[x - 1][y - 1];
	}
	if (x == 1 && y == 1)
		return 1;
	else if (x == 1) {    //在左边缘，只能从上面过来
                //对于数组说明，例如【5,4】位置，在数组中表示为res[4,3]，
                // 所以前一个位置在数组中为res[4,2]或res[3,3]。
		int fromTop=res[x-1][y-2]!=0? res[x - 1][y - 2] : dpPath(x, y - 1);
		res[x - 1][y - 2] = fromTop;
		return fromTop;
	}
	else if (y == 1) {  //在上边缘，只能从左面过来
		int fromLeft = res[x-2][y-1]!=0? res[x - 2][y - 1] : dpPath(x - 1, y);
		res[x - 2][y - 1] = fromLeft;
		return fromLeft;
	}
	else {
		//从左边过来
		int fromLeft = res[x-2][y - 1] != 0 ? res[x-2][y - 1] : dpPath(x-1, y );
		res[x - 2][y - 1] = fromLeft;
		//从上边过来
		int fromTop = res[x - 1][y - 2] != 0 ? res[x - 1][y - 2] : dpPath(x, y - 1);
		res[x - 1][y - 2] = fromTop;
		return fromLeft + fromTop;
	}
}
int uniquePaths(int m, int n) {
	res = new int*[m];
	for (int i = 0;i < m;++i) {
		res[i] = new int[n];
	}
	for (int i = 0;i < m;++i) {
		for (int j = 0;j < n;++j) {
			res[i][j] = 0;
		}
	}
	return dpPath(m, n);
}