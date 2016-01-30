
package org.usfirst.frc.team1559.robot;

import edu.wpi.first.wpilibj.IterativeRobot;


public class Robot extends IterativeRobot {
	
	SocketClient socket = new SocketClient();

	
	public void robotInit() {
		
		
	}

	public void autonomousInit() {
		
		socket.read();
		
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