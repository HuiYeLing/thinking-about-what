public class Student {
    int ID;
    int grade;
    Student(){
        this.ID = 1;
        this.grade = 1;
    }
    Student(int id, int grade){
        this.ID = id;
        this.grade = grade;
    }
    void say(){
        System.out.println("Ñ§ºÅ£º" + ID + "£¬Äê¼¶£º" + grade);
    }
}
