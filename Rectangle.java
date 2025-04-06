//Rectangle  class has the data fields width and height and the associated get and setmethods.
//Makanaka Mangwanda
//30 September 2024

public class Rectangle extends Shape{

//instance variables
private double width;
private double height;

//no argumant constructor
public Rectangle(){
this.width = 0;
this.height = 0;
}


public Rectangle(double width, double height){
this.width = width;
this.height = height;
}

public Rectangle(double width,double height, String color,boolean isFilled){
super(color,isFilled);
this.width = width;
this.height = height;
}

//get the area
public double getArea(){
return width*height;
}

//get the perimeter
public double getPerimeter(){
return 2*height + 2*width;
}

//get the height
public double getHeight(){
return height;
}

public double getWidth(){
return width;
}

public void setHeight(double height){
this.height = height;
}


public void setWidth(double width){
this.width = width;
}

 //check equality
public boolean equals(Rectangle other){
if(other == null){
return false;
}

return this.width == (other.width) && this.height == (other.height) && this.getColor().equals(other.getColor()) && this.isFilled() == (other.isFilled());
}



//convert to string
public String toString(){
return width + " " + height + " ";
}

}























