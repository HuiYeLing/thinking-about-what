public class UpDemo {
    public static void main(String[] args) {
        Animal a=new Animal();
        System.out.println(a.age);
        a.eat();
        Tiger t=new Tiger();
        System.out.println(t.name);
        t.say();
        t.eat();

        System.out.println(t.age);//���������Ե��ø����е�����
        Animal a1=new Tiger();//����ת�ͣ��Զ�ת�ͣ���������ָ���������
        //a1����һ��Animal��������ֻ�ܵ���Animal���еķ���
        a1.eat();
        System.out.println(a1.age);
        //a1.say();//������Ϊa1��Animal���͵ģ���Animal����û��say()����
        
        Object o=new Tiger();
    }
}
