public interface IShape
{
    double GetArea(); // only declares what needs to be done
}

public class Circle : IShape
{
    private double radius;

    public Circle(double r) => radius = r;

    public double GetArea() => Math.PI * radius * radius; // implementation hidden from user
}