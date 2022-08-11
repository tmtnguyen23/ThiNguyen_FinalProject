from math import pi as p

def volume_sphere(radius:float) -> float:
    """
    Function to compute the volume of sphere
    :param radius:  radius of the sphere
    :return: volume of the sphere
    """
    if type(radius) != int and type(radius) != float:
        raise TypeError('String input')
    if radius <= 0:
        raise ValueError('Not positive')
    else:
        return (4/3)*p*(radius**3)

def volume_sphere_nopi(radius:float) -> float:
    """
    Function to compute the multiplications of other components in the sphere-volume formula without pi
    :param radius: radius of the sphere
    :return: multiplications of (4/3) and the radius cubed
    """
    if type(radius) != int and type(radius) != float:
        raise TypeError('String input')
    if radius <= 0:
        raise ValueError('Not positive')
    else:
        return (4/3)*(radius**3)

def volume_cube(side: float) -> float:
    """
    Function to compute the volume of cube
    :param side: side of the cube
    :return: volume of the cube
    """
    if type(side) != int and type(side) != float:
        raise TypeError('String input')
    if side <= 0:
        raise ValueError('Not positive')
    else:
        return side**3

def volume_cylinder(radius: float, height: float) -> float:
    """
    Function to compute the volume of cylinder
    :param radius: the radius of the cylinder's base
    :param height: the height of the cylinder
    :return: volume of the cylinder
    """
    if (type(height) != int and type(height) != float) or (type(radius) != int and type(radius) != float):
        raise TypeError('String input')
    if height <= 0 or radius <= 0:
        raise ValueError('Not positive')
    else:
        return p*(radius**2)*height

def volume_cylinder_nopi(radius: float, height:float) -> float:
    """
    Function to compute the multiplications of other components in the cylinder-volume formula without pi
    :param radius: radius of the cylinder's base
    :param height: height of the cylinder
    :return: result of the multiplication of the height and the radius squared
    """
    if (type(height) != int and type(height) != float) or (type(radius) != int and type(radius) != float):
        raise TypeError('String input')
    if height <= 0 or radius <= 0:
        raise ValueError('Not positive')
    else:
        return (radius**2)*height

def volume_cone(radius:float, height:float) -> float:
    """
    Function to compute the volume of the cone given its height and radius of its base
    :param radius: radius of the cone's base
    :param height: height of the cone
    :return: volume of the cone
    """
    if (type(height) != int and type(height) != float) or (type(radius) != int and type(radius) != float):
        raise TypeError('String input')
    if height <= 0 or radius <= 0:
        raise ValueError('Not positive')
    else:
        return (1/3)*height*p*(radius**2)

def volume_cone_nopi(radius: float, height: float)-> float:
    """
    Function to compute the multiplications of other components without pi
    :param radius: radius of the cone's base
    :param height: height of the cone
    :return: result of the multiplication of (1/3) with the height and the radius squared
    """
    if (type(height) != int and type(height) != float) or (type(radius) != int and type(radius) != float):
        raise TypeError('String input')
    if height <= 0 or radius <= 0:
        raise ValueError('Not positive')
    else:
        return (1/3)*height*(radius**2)

def volume_rcpr(width: float, length: float, height: float) -> float:
    """
    Function to compute the volume of the rectangular prism
    :param width: width of the base
    :param length: length of the base
    :param height: height of the rectangular prism
    :return: volume of the rectangular prism
    """
    if (type(height) != int and type(height) != float) or (type(length) != int and type(length) != float) or (type(width) != int and type(width) != float):
        raise TypeError('String input')
    if height <= 0 or length <= 0 or width <= 0:
        raise ValueError('Not positive')
    else:
        return height*length*width
