import java.util.Scanner;
public class GuessWordGame03 {
    public static void main(String[] args) {
        System.out.println("猜字母游戏2");
        //接受自定义方法返回的4个字母
        char[] chrs=gen();
        System.out.println(chrs);
        boolean gameflag=true;
        int times=0;
        while(gameflag==true){
            System.out.print("请输入你猜测的字符串:");
            Scanner in=new Scanner(System.in);
            String inputword=in.next().toUpperCase().trim();
            char[] inchrs=inputword.toCharArray();

        int[] result=check(chrs,inchrs);
        if(inputword.equals("EXIT")){
        System.out.println("结束!");
        break;
        }
        times++;
        result[0]=result[0]-result[1];
        if(result[1]==4){
        System.out.println("全对!");
        gameflag=false;
        }              
        else {
            System.out.println("本次猜测为:"+result[1] + "A"+ result[0]+"B"+",已经猜了"+times+"次");
        }
    }
    }
    public static char[] gen(){
        char[] letters={'A','B','C','D','E','F','G','H','I','J'};
        boolean[] flags=new boolean[letters.length];
        char[] chrs=new char[4];
        for(int i=0;i<flags.length;i++){
            flags[i]=false;
        }
        int count=0;
        while(count<4){
            int index=(int)(Math.random()*10);
            if(flags[index]==false){
                chrs[count]=letters[index];
                flags[index]=true;
                count++;
            }
        }
        return chrs;
    }
    public static int[] check(char[] chrs,char[] inchrs)
    {
        int[] result=new int[]{0,0};
        for(int i=0;i<chrs.length;i++){
            for(int j=0;j<inchrs.length;j++){
                if(chrs[i]==inchrs[j]){
                    result[0]++;
                    if(i==j){
                        result[1]++;
                    }
                }
            }
        }
         return result;
    }
}
   