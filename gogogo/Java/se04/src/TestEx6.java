public class TestEx6 {
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
    }
    finally{
        System.out.println("all");
    }
}
}
