import java.util.Scanner;
public class GuessWordGame02 {
public static void main(String[] args) {
        //�����abcdefgh��ȡ��4����ĸ
        //Ҫ�����ظ����û�����һ���ַ�����������ַ������бȽϣ��ȽϽ����A��B��ʾ
        //A��ʾ��ĸ��λ�ö���ȷ��B��ʾ��ĸ��ȷ��λ�ò���ȷ
        //�����������ABCD���û�����CGHD������1B����ʾ��һ����ĸ��ȷ��λ�ò���ȷ��1A����ʾ��һ����ĸ��ȷ��λ����ȷ
        //�������1B1A

        //1.��Ϸ���в����˳�
        //2.����exit������;�˳�
        //3.���Դ�Сд
        //4.�²������Ҫ��ʾ�Ѿ��²�Ĵ���
        System.out.println("����ĸ��Ϸv2.0");
        
        char[] letters = new char[]{'A','B', 'C', 'D', 'E', 'F', 'G', 'H'};//��ĸ����
        boolean [] flags=new boolean[letters.length];//���������ĸ�Ƿ�ʹ��
        char[] chrs=new char[4];//������������4����ĸ
        for(int i=0;i<flags.length;i++){
            flags[i]=false;//��ʼ��Ϊfalse
        }
        int cout=0;//������
        while (cout<4) //����4�� 
        {
            int num = (int) (Math.random() * letters.length);//[0,8)
            //num������������±�0~7 
            if (flags[num]==false)//�����±�Ϊnum����ĸû�б�ʹ��
            {
               chrs[cout] = letters[num];//����ĸ��������
               flags[num]=true;//��ĸ��ʹ��
               cout++;//����
            }
        }
        System.out.println(chrs);

        //1.
        boolean gameflag=true;
        int times=0;
        while (gameflag==true) 
        {
            //���²��ַ������������Ĵ���ճ������
        System.out.print("��������µ���ĸ��");
        Scanner in=new Scanner(System.in);
        //��������ַ���ת���ɴ�д��ȥ��ǰ��ո�
        String inputword=in.next().toUpperCase().trim();//������ַ���
        //��������ַ���ת��Ϊ�ַ�����
        char[] inchrs=inputword.toCharArray();//���ַ���ת��Ϊ�ַ�����
        //���������chrs�������inchrs���бȽ�
        //��űȽϽ��������
        //result[0]���B�ĸ��� rusult[1]���A�ĸ���
        int [] result=new int[]{0,0};//��űȽϽ��������
        //2.��;�˳�
            if (inputword.equals("EXIT")) 
            {
                System.out.println("��Ϸ��ǰ����");
                break;
            }

        for(int i=0;i<inchrs.length;i++){
            for(int j=0;j<chrs.length;j++)
            {
                if (inchrs[i]==chrs[j]) //��ĸ��ͬ
                {
                    result[0]++;
                    if(i==j)//λ����ͬ
                        result[1]++;
                }
            }
        }
            times++;
            result[0]=result[0]-result[1];//B�ĸ���
            if(result[1]==4) 
            {
            System.out.println("��ϲ�㣬�¶��ˣ�");
            gameflag=false;//ȫ�����ˣ�����ѭ��
            }

            else System.out.println(result[1]+"A"+result[0]+"B"
            +"�Ѿ�����"+times+"����");
        }
    }
}
        