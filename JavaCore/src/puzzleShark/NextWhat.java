package puzzleShark;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;

public class NextWhat {
	
	public static int whomShouldIeat(int sharkWgt,ArrayList<Integer> fishes) {
		
		ArrayList<Integer> newfish=new ArrayList<Integer>();
		for (Iterator<Integer> iterator = fishes.iterator(); iterator.hasNext();) {
			Integer integer = (Integer) iterator.next();
			if(integer<sharkWgt) {
				newfish.add(integer);
			}
			
		}
		if(newfish.isEmpty()) {
			return -1;
		}else {
			int min=Collections.max(newfish);
			return min;
		}
		
	}

}
