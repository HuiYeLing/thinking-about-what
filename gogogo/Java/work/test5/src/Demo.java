
public class Demo {
    public static void main(String[] args) {
        MainSata mainSata = new MainSata();
        CheckSata checkSata = new CheckSata();
        LookSata lookSata = new LookSata();

        mainSata.useSATA(checkSata);
        mainSata.useSATA(lookSata);
    }
}