public class Computer {
    private int cpu;
    private String type;
    private String system;

    public Computer(){
        this.cpu = 7;
        this.type = "Ì¨Ê½»ú";
        this.system = "Windows";
    }
    public Computer(int cpu, String type, String system){
        this.cpu = cpu;
        this.type = type;
        this.system = system;
    }
    public int getCpu() {
        return cpu;
    }
    public String getType() {
        return type;
    }
    public void setCpu(int cpu) {
        this.cpu = cpu;
    }
    public void setType(String type) {
        this.type = type;
    }
    public void setSystem(String system) {
        this.system = system;
    }
    
}
