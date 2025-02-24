package shapes;

public class circle {
private double radius;
	
	public circle(double radius) {
		this.radius = radius;
	}
	
	public double calculateArea() {
		return 3.14*radius*radius;
	}
	public double calculateCircum() {
		return 2*3.14*radius;
	}
}
