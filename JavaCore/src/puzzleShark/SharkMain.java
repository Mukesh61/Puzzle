package puzzleShark;
import puzzleShark.NextWhat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class SharkMain {

	public static void main(String[] args) {
		ArrayList<Integer> fishTank=new ArrayList<Integer>();
		System.out.println("Please enter the weigth of Shark");
		Scanner scan= new Scanner(System.in);
//		int sharkWeight=scan.nextInt();
		String sW=scan.nextLine();
		int sharkWeight=Integer.parseInt(sW);
		System.out.println("Please enter fishes in the Tank hit enter to end");
		while(true) {
			sW=scan.nextLine();
//			fishTank.add(Integer.parseInt(sW));
			if(sW.equals("")) {
//				System.out.println("breaking it");
				break;
			}else {
			fishTank.add(Integer.parseInt(sW));
		}
		}
		System.out.println("Fish in the Tank are"+fishTank);
		
		
		scan.close();
//		fishTank.add(3);
//		fishTank.add(4);
//		fishTank.add(10);
//		fishTank.add(20);
//		fishTank.add(50);
//		fishTank.add(500);
		int eat;
		int indexi;
		int maxFish;
		int minFish;
		int swapFish;
		while(!fishTank.isEmpty()) {
			eat=NextWhat.whomShouldIeat(sharkWeight,fishTank);
//			System.out.println("after function call "+eat);
			if(eat==-1) {
				maxFish=Collections.max(fishTank);
				minFish=Collections.min(fishTank);
				swapFish=minFish-sharkWeight+1;
				fishTank.add(swapFish);
				indexi=fishTank.indexOf(maxFish);
				fishTank.remove(indexi);
				System.out.println("i am adding a fish of "+swapFish+"removing the "+maxFish);
				
				
			}else {
				indexi=fishTank.indexOf(eat);
				fishTank.remove(indexi);
				sharkWeight+=eat;
				System.out.println("I am eating a lovely fish of weight "+eat);
				
			}
			
		}
//		System.out.println(NextWhat.whomShouldIeat(sharkWeight,fishTank));
		// TODO Auto-generated method stub

	}

}
