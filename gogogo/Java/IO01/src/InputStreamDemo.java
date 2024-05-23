import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.File;
public class InputStreamDemo {
    public static void main(String[] args) {
        try {
            InputStream in = new FileInputStream(new File("D:\\study\\test.txt"));
            byte[] buf = new byte[in.available()];
            in.read(buf);
            System.out.println(new String(buf));
        } catch (Exception e) {
            e.printStackTrace();
        } 
        InputStream in = null;
        try {
            in = new FileInputStream(new File("D:\\study\\test.txt"));
            byte[] buf = new byte[in.available()];
            in.read(buf);
            System.out.println(new String(buf));
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                {
                    in.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
