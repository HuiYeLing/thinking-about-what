import java.io.File;
import java.io.IOException;

public class demo01{
    public static void main(String[] args)  {
        File file = new File("D:\\study\\test.txt");
        boolean flag=file.exists();//判断文件是否存在
        //  try{
            // if (flag) 
            // {
            //     file.delete();//删除文件
            //     System.out.println("文件已经存在，已经删除文件");
            // }
            // else{
                // file.createNewFile();
                // System.out.println("文件不存在，已经创建文件");
                System.out.println(file.isFile()==true?"是文件":"不是文件");
                System.out.println(file.isDirectory()==true?"是目录":"不是目录");
                System.out.println("相对路径"+file.getPath());
                System.out.println("绝对路径"+file.getAbsolutePath());
                System.out.println("文件名"+file.getName());
                System.out.println("文件长度"+file.length());
            // }
           
        //  }catch(IOException e)
        //  {
        //     e.printStackTrace();
        // }
    }
}
