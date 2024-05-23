import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.File;

public class FileCopy {
    public static void main(String[] args) {
        // 文件复制
        InputStream in = null;
        OutputStream out = null;
        try {
            in = new FileInputStream(new File("D:\\study\\test.txt"));
            out = new FileOutputStream("D:\\study\\test1.txt");     
            byte [] buf = new byte[10]; // 开辟10个字节的缓冲区
            int len;
            // read的返回值是实际读取的文件大小,如果没有读取内容,返回-1
            while((len=in.read(buf))!=-1) {
                out.write(buf,0,len);
            }
        } catch(IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (out != null) out.close();
                if(in != null) in.close();
            } catch(IOException e) {
                e.printStackTrace();
            }
        }
    }
}