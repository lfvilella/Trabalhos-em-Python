def tag(name, **attributes):
    result = "<" + name
    for key, value in attributes.items():
        result += f' {key}="{str(value)}"'
    result += ">"
    return result


if __name__ == "__main__":
    print(tag("img", src="image.jpg", alt="Some Image", border=1))

    data_tag = {
        "name": "img",
        "src": "image2.jpg",
        "alt": "Some Image 2",
        "border": 2,
    }
    print(tag(**data_tag))
