import java.util.Scanner;

import javax.print.DocFlavor.STRING;

public class StringDemo08 {
    public static void main(String[] args) {
        // String str="123456,,,456,,546,,,4886,,";
        // String[] arr=str.split(",");

        String str1="12345adaa456aa54dddd4886aa";
        String[] arr1=str1.split("[a-z]+");
        for(int i=0;i<arr1.length;i++)
        System.out.println(arr1[i].toString());
        Scanner scan=new Scanner(System.in);
        String filename=scan.next().trim();
        String fileregex="\\.";
        String[] filea=filename.split(fileregex);
        filename=System.currentTimeMillis()+"."+filea[1];
        System.out.println(filename);
        scan.close();
    }
}
