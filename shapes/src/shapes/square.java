package shapes;

public class square {
private double side;
	
	public square(double side) {
		this.side=side;
	}
	public double calculateArea() {
		return side*side;
	}
	public double calculatePerimeter() {
		return 4 * side;
	}
}
