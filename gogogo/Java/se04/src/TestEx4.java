public class TestEx4 {
    public static void main(String[] args) {
        try{
        String teacher[]={"1","2","3"};
        for (int i = 0; i < 4; i++) {
            System.out.println(teacher[i]);
        }
    }catch(Exception e){
        System.out.println("Hello World!");
        System.exit(0);
    }
    finally{
        System.out.println("The index is out of bounds.");
    }         
}
}
