public class TestEx7 {
    public static void main(String[] args) {
        System.out.println("now");
        try{
            System.out.println("is");
            throw new NullPointerException("the ");
        }catch(NullPointerException e){
            System.out.println("e.getmessage()");
        }
        finally{
            System.out.println("time");
        }
    }
}
