public class TestEx5 {
    public static void main(String[] args) {
        try{
        String teacher[]={"1","2","3"};
        for (int i = 0; i < 4; i++) 
        {
            System.out.println(teacher[i]);
        }
    }
    catch(ArrayIndexOutOfBoundsException e)
    {
        System.out.println("The index is out of bounds.");
    }catch(RuntimeException e){
        System.out.println("The index is out of bounds.");
    }
    
    catch(Exception e){
        System.out.println("Hello World!");
        System.exit(0);
    }
    finally{
        System.out.println("all");
    }
}
}
//ArrayIndexOutOfBoundsException是RuntimeException的子类，所以catch(RuntimeException e)会捕获到ArrayIndexOutOfBoundsException异常