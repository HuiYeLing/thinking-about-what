import java.util.Scanner;
public class GuessWordGame03 {
    public static void main(String[] args) {
        System.out.println("����ĸ��Ϸ2");
        //�����Զ��巽�����ص�4����ĸ
        char[] chrs=gen();
        System.out.println(chrs);
        boolean gameflag=true;
        int times=0;
        while(gameflag==true){
            System.out.print("��������²���ַ���:");
            Scanner in=new Scanner(System.in);
            String inputword=in.next().toUpperCase().trim();
            char[] inchrs=inputword.toCharArray();

        int[] result=check(chrs,inchrs);
        if(inputword.equals("EXIT")){
        System.out.println("����!");
        break;
        }
        times++;
        result[0]=result[0]-result[1];
        if(result[1]==4){
        System.out.println("ȫ��!");
        gameflag=false;
        }              
        else {
            System.out.println("���β²�Ϊ:"+result[1] + "A"+ result[0]+"B"+",�Ѿ�����"+times+"��");
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
   