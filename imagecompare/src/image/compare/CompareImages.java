package image.compare;

import java.awt.Image;
import java.awt.image.PixelGrabber;
import java.io.File;
import java.util.Arrays;

import javax.swing.ImageIcon;

public class CompareImages {

	public static void main( String[] args ) throws Exception {
		
		final int TEST_PASSED = 0;
		final int TEST_FAILED = 1;
		final int FILE_NOT_FOUND = 2;
				
		
		File file1 = new File( args[0] );
		File file2 = new File( args[1] );
		
		boolean paramExpectDiff = Boolean.parseBoolean(args[2]);
		boolean imageEqual = false;
		int compareResult = TEST_PASSED;
		
		if (file1.exists() == false || file2.exists() == false) {
			System.exit(FILE_NOT_FOUND);
		}

		Image image1 = (new ImageIcon(file1.toString())).getImage();
		Image image2 = (new ImageIcon(file2.toString())).getImage();
		PixelGrabber grab1 = new PixelGrabber(image1, 0, 0, -1, -1, false);
		PixelGrabber grab2 = new PixelGrabber(image2, 0, 0, -1, -1, false);
		
		int data1[] = null;
		int width1 = 0;
		int height1 = 0;
		int width2 = 0;
		int height2 = 0;
		
		if (grab1.grabPixels()) {
			width1 = grab1.getWidth();
			height1 = grab1.getHeight();
			data1 = new int[width1 * height1];
			data1 = (int[])(int[]) grab1.getPixels();
		}
		
		int data2[] = null;
		if(grab2.grabPixels()) {
			width2 = grab2.getWidth();
			height2 = grab2.getHeight();
			data2 = new int[width2 * height2];
			data2 = (int[])(int[]) grab2.getPixels();
		}
		
		imageEqual = Arrays.equals(data1,  data2);
		if (paramExpectDiff) {
			// Differences were expected but the images were the same
			if (!imageEqual )
				compareResult = TEST_FAILED;
		} else {
			if (imageEqual)
				compareResult = TEST_FAILED;
		}
		
		System.exit(compareResult);
			
		}
}