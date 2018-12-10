package concept;

import java.util.HashMap;

public class HashMapExample {

	public static void main(String[] args) {

		HashMap<Integer,String> newmap=new HashMap<Integer, String>();
		newmap.put(1, "Mukesh");
		newmap.put(2,"Bhegna Shree");
		System.out.println("output "+newmap.get(2));

	}

}
