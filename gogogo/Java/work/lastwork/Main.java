import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

// School类定义
class School {
    String id;
    String name;
    String city;

    public School(String id, String name, String city) {
        this.id = id;
        this.name = name;
        this.city = city;
    }

    @Override
    public String toString() {
        return "School{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", city='" + city + '\'' +
                '}';
    }
}

// School的外部比较器
class SchoolComparator implements Comparator<School> {
    @Override
    public int compare(School s1, School s2) {
        int idCompare = s1.id.compareTo(s2.id);
        if (idCompare == 0) {
            // ID相同，按学校名称降序排序
            return s2.name.compareTo(s1.name);
        }
        return idCompare; // 按ID升序排序
    }
}

public class Main {
    public static void main(String[] args) {
        List<School> schools = new ArrayList<>();
        schools.add(new School("002", "清华", "北京"));
        schools.add(new School("001", "北大", "北京"));
        schools.add(new School("001", "浙大", "浙江"));

        Collections.sort(schools, new SchoolComparator());

        for (School school : schools) {
            System.out.println(school);
        }
    }
}