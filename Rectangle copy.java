// a program of a rectangle object with an additional length and width, inherited from the first object
// Makanaka Mangwanda
// 27 September 2024

public class Rectangle extends Shape{

//instance variables
private double length;
private double width;

public Rectangle(Rectangle other){
super(other);
this.length = other.length;
this.width = other.width;
}

//constructor
public Rectangle(String name,String colour, double length, double width){
super(name,colour);//calling the parent class
this.length = length;
this.width = width;
}


//converting to string
public String toString(){
return super.toString() + "Length " + length + " Width " + width;
}


}