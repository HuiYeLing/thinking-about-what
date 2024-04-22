import java.util.InputMismatchException;
import java.util.Scanner;
public class TextEx8 {
    
    //throws
    public static void p()throws InputMismatchException{
        int appleNum=0;
        int stuNum=0;
        System.out.println("/");
        Scanner scan=new Scanner(System.in);
        System.out.println("Please input the number of apples:");
        appleNum=scan.nextInt();
        while (stuNum==0) {
            System.out.println("The number of students can't be 0.");
            stuNum=scan.nextInt();
        }
        System.out.println("Each student can get "+appleNum/stuNum+" apples.");
        System.out.println("There are apples left.");
    }
        
    public static void main(String[] args) {
        try{
            p();
        }catch(InputMismatchException e){
            System.out.println("Please input an integer.");
        }
    }
        
    
}
