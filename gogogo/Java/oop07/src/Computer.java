public class Computer {
        private int cpu;
        private String type;
        private String system;  
        public final int MACID;
        public Computer(){
            super();
            this.MACID = 1001;
        }
        public Computer(int cpu, String type, String system,int mACID){
            super();
            this.cpu = cpu;
            this.type = type;
            this.system = system;
            MACID=mACID;
        }
}
