interface SAS {
    void start();
    void stop();
}

class HardSas implements SAS {
    public void start() {
        System.out.println("HardSas 开始工作");
    }

    public void stop() {
        System.out.println("HardSas 停止工作");
    }
}
class RigidSas implements SAS {
    public void start() {
        System.out.println("RigidSas 开始工作");
    }

    public void stop() {
        System.out.println("RigidSas 停止工作");
    }
}

class MainBoard {
    public void useSAS(SAS sas) {
        sas.start();
        sas.stop();
    }
}

public class Demo {
    public static void main(String[] args) {
        MainBoard mainBoard = new MainBoard();
        HardSas hardSas = new HardSas();
        RigidSas rigidSas = new RigidSas();

        mainBoard.useSAS(hardSas);
        mainBoard.useSAS(rigidSas);
    }
}