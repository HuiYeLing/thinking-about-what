import java.util.Scanner;

public class Man {
public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    while (true) {
        System.out.println("-------------------------------");
        System.out.println("|  蓝桥Java工程师管理系统  |");
        System.out.println("-------------------------------");
        System.out.println("1.输入Java工程师资料");
        System.out.println("2.删除指定Java工程师资料");
        System.out.println("3.查询Java工程师资料");
        System.out.println("4.修改Java工程师资料");
        System.out.println("5.计算Java工程师的月薪");
        System.out.println("6.保存新添加的工程师资料");
        System.out.println("7.对Java工程师信息排序（1编号升序，2姓名升序）");
        System.out.println("8.输出所有Java工程师信息");
        System.out.println("9.清空所有Java工程师信息");
        System.out.println("10.打印Java工程师信息");
        System.out.println("11.从文件重新导入Java工程师数据");
        System.out.println("0.结束（编辑工程师信息后提示保存）");
        System.out.println("请输入您的选择：");
        int usernum=scan.nextInt();
        switch (usernum) {
            case 1:System.out.println("本模块功能未实现");
                break;
                case 2:System.out.println("本模块功能未实现");
                break;
                case 3:System.out.println("本模块功能未实现");
                break;
                case 4:System.out.println("本模块功能未实现");
                break;
                case 5:
               
                System.out.println("请输入Java工程师底薪：");
                int dixin=scan.nextInt();
                System.out.println("请输入Java工程师月工作完成分数(最小值为0，最大值150)：");
                int fenshu=scan.nextInt();
                System.out.println("请输入Java工程师实际工作天数：");
                double date=scan.nextInt();
                System.out.println("请输入Java工程师应扣保险数：");
                double baoxian=scan.nextInt();
                double salary = dixin + fenshu * date - baoxian;
                System.out.println("Java工程师的月薪为：" + String.format("%.1f", salary));

                break;
                case 6:System.out.println("本模块功能未实现");
                break;
                case 7:System.out.println("本模块功能未实现");
                break;
                case 8:System.out.println("本模块功能未实现");
                break;
                case 9:System.out.println("本模块功能未实现");
                break;
                case 10:System.out.println("本模块功能未实现");
                break;
                case 11:System.out.println("本模块功能未实现");
                break;
                case 0:System.out.println("程序结束！");
                System.exit(0);
                break;
                default:System.out.println("输入错误，请重新输入！");
                break;
        }
        
       
    }
}
}