// a program of a circle object with an additional radius, inherited from the first object
// Makanaka Mangwanda
// 27 Septemeber 2024

public class Circle extends Shape{

//instance variables
private double radius;

public Circle(Circle other){
super(other);
this.radius = other.radius;
}

//constructor
public Circle(String name, String colour,double radius){
super(name,colour);
this.radius = radius;
}

public String toString(){
return super.toString() + "Radius " + radius;
}

}