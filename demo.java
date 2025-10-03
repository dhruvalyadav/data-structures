
class Demo{
    public static void main(String args[]){
        int nums[][]=new int[3][4];
        for(int i=0;i<3;i++){
            for(int j=0;j<4;j++){
                nums[i][j]= (int) (Math.random()*100);
                System.out.print(nums[i][j]+" ");
            }
            System.out.println();
        }
    }
}


class Moblie{
    String brand;
    int price;
    static String name;

    public Moblie(){
        brand="";
        price=2000;
    }

    public void show(){
        System.out.println(brand+" "+price+" "+name);
    }
    public static void main(String[] args) {
        Moblie a= new Moblie();
        
    }
}