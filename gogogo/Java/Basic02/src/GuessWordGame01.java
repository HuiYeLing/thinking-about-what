import java.util.Scanner;
public class GuessWordGame01 {
public static void main(String[] args) {
        //随机从abcdefgh中取出4个字母
        //要求无重复，用户输入一个字符串，与组成字符串进行比较，比较结果用A和B表示
        //A表示字母和位置都正确，B表示字母正确但位置不正确
        //例如随机生成ABCD，用户输入CGHD，返回1B：表示有一个字母正确但位置不正确，1A：表示有一个字母正确且位置正确
        //结果就是1B1A
        System.out.println("猜字母游戏v1.0");
        char[] letters = new char[]{'A','B', 'C', 'D', 'E', 'F', 'G', 'H'};//字母数组
        boolean [] flags=new boolean[letters.length];//用来标记字母是否被使用
        char[] chrs=new char[4];//存放随机产生的4个字母
        for(int i=0;i<flags.length;i++){
            flags[i]=false;//初始化为false
        }
        int cout=0;//计数器
        while (cout<4) //产生4次 
        {
            int num = (int) (Math.random() * letters.length);//[0,8)
            //num是随机产生的下标0~7 
            if (flags[num]==false)//代表下标为num的字母没有被使用
            {
               chrs[cout] = letters[num];//把字母放入数组
               flags[num]=true;//字母已使用
               cout++;//计数
            }
        }
        System.out.println(chrs);
        System.out.print("请输入你猜的字母：");
        Scanner in=new Scanner(System.in);
        String inputword=in.next();//输入的字符串
        //将输入的字符串转换为字符数组
        char[] inchrs=inputword.toCharArray();//将字符串转换为字符数组
        //随机产生的chrs和输入的inchrs进行比较
        //存放比较结果的数组
        //result[0]存放B的个数 rusult[1]存放A的个数
        for(int i=0;i<inchrs.length;i++){
            int [] result=new int[]{0,0};//存放比较结果的数组
            for(int j=0;j<chrs.length;j++)
            {
                if (inchrs[i]==chrs[j]) //字母相同
                {
                    result[0]++;
                    if(i==j)//位置相同
                    {
                        result[1]++;
                    }
                }
            }
            result[0]=result[0]-result[1];//B的个数
            if(result[1]==4) System.out.println("恭喜你，猜对了！");
            else
                System.out.println(result[1]+"A"+result[0]+"B");
        }
    }
}