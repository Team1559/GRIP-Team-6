
package org.usfirst.frc.team1559.robot;

import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.networktables.NetworkTable;


public class Robot extends IterativeRobot {
	
	NetworkTable table;
	
	
    public void robotInit() {
    	
    	table = NetworkTable.getTable("GRIP/myLinesReport");
    }
    
    
    public void autonomousInit() {
    	
    }
   
    
    public void autonomousPeriodic() {
    	
    	double[] x = new double[0];
    	while(true) {
    		double[] lines = table.getNumberArray("line", x);
    		for (double line : lines) {
    			System.out.println(line);
    		}
    		System.out.println("ayy lmao");
    	}
    }

    
    public void teleopInit() {
    	
    }
    
    
    public void teleopPeriodic() {
        
    }
    
    
    public void testPeriodic() {
    
    }
    
}
