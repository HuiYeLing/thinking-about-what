public class xiaoxing {
    public static void main(String[] args) {
        int n=5;
        for (int i = 0; i < n; i++) {
            // ��ӡ�ո�
            for (int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            // ��ӡ�Ǻ�
            for (int k = 0; k < 2 * i + 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
        for (int i = n - 2; i >= 0; i--) {
            // ��ӡ�ո�
            for (int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            // ��ӡ�Ǻ�
            for (int k = 0; k < 2 * i + 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
