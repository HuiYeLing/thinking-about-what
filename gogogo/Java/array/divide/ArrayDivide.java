import java.util.Scanner;
public class ArrayDivide {
    public static void main(String[] args) throws Exception {
        int d1[],d2[];
        int leng1,leng2;
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入两个数组的长度：");
        leng1=sc.nextInt();
        leng2=sc.nextInt();
        d1=new int[leng1];
        d2=new int[leng2];
        System.out.println("请输入第一个数组种的"+d1.length+"个整数：");
        for(int i=0;i<d1.length;i++){
            d1[i]=sc.nextInt();
        }   
        System.out.println("请输入第二个数组种的"+d2.length+"个整数：");
        for(int i=0;i<d2.length;i++){
            d2[i]=sc.nextInt();
        
        try{
            System.out.println(d1[i]+"/"+d2[i]+"="+(d1[i]/d2[i]));
        }catch(ArithmeticException e){
            System.out.println(e.getMessage());
        }catch(ArrayIndexOutOfBoundsException e){
            System.out.println(e.getMessage());
        }catch(Exception e){
            System.out.println("程序出现异常");
        }
    }
}
}
