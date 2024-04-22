public class TextEx3{
    public static void main(String[] args) { 
        //包括可能会报错的代码
        try{
        String teacher[]={"1","2","3"};
        for (int i = 0; i < 4; i++) {
            System.out.println(teacher[i]);
        }
    }
    //catch包括发生异常时应该执行的代码
    catch(Exception e){
        System.out.println("The index is out of bounds.");
    }
      
        System.out.println("Hello World!");
    }
}
