// a shape object with a name and colour and the other objects are inherited from this object
// Makanaka Mangwanda
// 27 September 2024

public class Shape{

//instance variables

private String name;
private String colour;

//constructor
public Shape(Shape shape){
this.name = shape.name;
this.colour = shape.colour;
}

//constructor
public Shape(String name, String colour){
this.name = name;
this.colour = colour;
}

//convert to string
public String toString(){
return name + " " + colour + " ";
}

}
