
package org.usfirst.frc.team1559.robot;

import edu.wpi.first.wpilibj.IterativeRobot;


public class Robot extends IterativeRobot {
	
	NetworkTableClient table = new NetworkTableClient();

	public void robotInit() {
		
		
	}

	public void autonomousInit() {
		
		table.run();
	}

	public void autonomousPeriodic() {
		
		
	}

	public void teleopInit() {

	}

	public void teleopPeriodic() {

	}

	public void testPeriodic() {

	}

}