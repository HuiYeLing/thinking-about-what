package test6;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class School {
    private int id;
    private String name;
    private String city;
    public School(){
        super();
    }
    public School(int id, String name, String city) {
        super();
        this.id = id;
        this.name = name;
        this.city = city;
    }
     
    public String toString() {
        return "School [id=" + id + ", name=" + name + ", city=" + city + "]";
    }
}