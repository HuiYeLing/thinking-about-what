import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.Map.Entry;
public class test02 {
    public static void main(String[] args) {
        //创建一个单值集合List<String>
        //创建一个双值集合Map<String,Integer>
        List<String> list = new ArrayList<String>();
        list.add("aa");
        System.out.println("单值集合"+list.get(0));
        Map<String,Integer> map = new HashMap();
        map.put("s01",3);
        map.put("s02",1);
        map.put("s03",2);
        //将key和value相加为entry
        Set<Entry<String,Integer>> entries = map.entrySet();
        for(Entry<String,Integer> entry:entries)//遍历entry,从entry中取出key和value
            System.out.println(entry.getKey()+" "+entry.getValue());
    }
}
