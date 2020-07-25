class Position:
    def __init__(self, latitude, longitude):
        self._latitude = self.check_latitude(latitude)
        self._longitude = self.check_longitude(longitude)

    def check_latitude(self, latitude):
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude out of range")
        return latitude

    def check_longitude(self, longitude):
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude out of range")
        return longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"

    def __repr__(self):
        return (
            f"{typename(self)}"
            f"(latitude={self.latitude}, longitude={self.longitude})"
        )

    def __str__(self):
        return (
            f"{abs(self.latitude)} {self.latitude_hemisphere}, "
            f"{abs(self.longitude)} {self.longitude_hemisphere}"
        )

    def __format__(self, format_spec):
        component_format_spec = ".2f"
        _, dot, sufix = format_spec.partition(".")
        if dot:
            num_decimal_places = int(sufix)
            component_format_spec = f".{num_decimal_places}f"

        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return (
            f"{latitude} {self.latitude_hemisphere}, "
            f"{longitude} {self.longitude_hemisphere}"
        )


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


def typename(obj):
    return type(obj).__name__


if __name__ == "__main__":
    position = Position(1, 2)
    earth = EarthPosition(3, 4)
    mars = MarsPosition(5, 6)

    print(repr(position), str(position), format(position, ".3") )
    print(repr(earth), str(earth), format(earth, ".5"))
    print(repr(mars), str(mars), format(mars))
