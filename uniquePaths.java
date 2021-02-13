class Solution {
    public int uniquePaths(int m, int n) {
        int[][] ds = new int[m][n];
        for(int i=0;i<ds.length;i++){
            ds[i][0] = 1;
        }
        
        for(int i=0;i<ds[0].length;i++){
            ds[0][i] = 1;
        }
        
        for(int i=1;i<ds.length;i++){
            for(int j=1;j < ds[i].length;j++){
                ds[i][j] = ds[i-1][j] + ds[i][j-1];
            }
        }
        return ds[m-1][n-1];
    }
}
