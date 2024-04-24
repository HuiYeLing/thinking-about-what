public class StudentBize {
    Student[] students=new Student[30];

    public boolean addStudent(Student student)
    {
        int index=-1;
        for(int i=0;i<students.length;i++)
        {
            if(students[i]==null)
            {
                index=i;
                break;
            }
        }
        if (index==-1) {
            System.out.println("数组已满");
            return false;
        }
        else{
            students[index]=student;
            return true;
        }
    }
    public void showStudent()
    {
        for(int i=0;i<students.length;i++)
        {
            if(students[i]!=null)
            System.out.println(students[i].getName()+students[i].getAge());
        }
    }
}
