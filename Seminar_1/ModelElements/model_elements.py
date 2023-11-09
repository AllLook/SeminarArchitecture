class Point3D:
    pass


class Angle3D:
    pass


class Color:
    pass


class Texture:
    pass


class Poligon:
    points: Point3D
    poligonalmodel: PoligonalModel  # здесь не стыкуется, PoligonalModel должен иметь Poligon, а Poligon должен иметь PoligonalModel, но они не видят друг друга пока не обьявлено выше, замена местами дает такую же проблему


class PoligonalModel:
    poligons: Poligon
    textures: Texture


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def rotate(self, Angle3D):  # вместо void возвращает что то или нет
        pass

    def move(self, Point3D):
        pass


class Camera:
    location: Point3D
    angle: Angle3D

    def rotate(self, Angle3D):  # вместо void возвращает что то или нет
        pass

    def move(self, Point3D):
        pass


class Scene:
    id: int
    models: PoligonalModel
    flashed: Flash

    def method1(self, temp: type):
        return type

    def method1(self, temp1: type, type2: type):
        return type
