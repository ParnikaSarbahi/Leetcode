class Solution {
    public int trap(int[] height) {
        int l=height.length;
        int[] leftboundary=new int[l];
        int[] rightboundary=new int[l];

        leftboundary[0]=height[0];
        for(int i=1;i<l;i++){
            leftboundary[i]=Math.max(leftboundary[i-1],height[i]);  
        }

        rightboundary[l-1]=height[l-1];
        for(int i=l-2;i>=0;i--){
            rightboundary[i]=Math.max(rightboundary[i+1],height[i]);
        }
        

        int wl,trappedwater=0;
        for(int j=0;j<l;j++){
            wl=Math.min(leftboundary[j],rightboundary[j]);
            trappedwater+=(wl-height[j]);
        }
        return trappedwater;
    }
}
