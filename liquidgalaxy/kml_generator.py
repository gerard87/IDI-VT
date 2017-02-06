import os

def create_line_kml(line, towers):
    filename = "static/kml/" + line.name + ".kml"
    if os.path.exists(filename):
            os.system("rm " + filename)
    os.system("touch " + filename)
    image1 = "http://maps.google.com/mapfiles/kml/shapes/star.png"
    image2 = "http://gsoc16.herokuapp.com/static/img/icon_white_tower.png"

    with open(filename, "w") as kml_file:
        kml_file.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
            "<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n" +
            "\t<Document>\n" +

            "\t<Style id=\"" + line.name + "\">\n" +
            "\t\t\t<IconStyle>\n" +
            "\t\t\t\t<scale>0.4</scale>\n" +
            "\t\t\t\t<Icon>\n" +
            "\t\t\t\t\t<href>" + image1 + "</href>\n" +
            "\t\t\t\t</Icon>\n" +
            "\t\t\t</IconStyle>\n" +
            "\t\t<LabelStyle>\n" +
            "\t\t\t<color>9900ffff</color>\n" +
            "\t\t\t<scale>1</scale>\n" +
            "\t\t</LabelStyle>\n" +
            "\t\t<LineStyle>\n"+
            "\t\t\t<color>990000ff</color>\n" +
            "\t\t\t<width>2</width>\n" +
            "\t\t</LineStyle>\n" +
            "\t\t<PolyStyle>\n" +
            "\t\t\t<color>997f7fff</color>\n" +
            "\t\t\t<fill>1</fill>\n" +
            "\t\t\t<outline>1</outline>\n" +
            "\t\t</PolyStyle>\n" +
            "\t</Style>\n" +

            "\t<Style id=\"tower\">\n" +
            "\t\t<IconStyle>\n" +
            "\t\t\t<scale>2.0</scale>\n" +
            "\t\t\t<Icon>\n" +
            "\t\t\t\t<href>" + image2 + "</href>\n" +
            "\t\t\t</Icon>\n" +
            "\t\t</IconStyle>\n" +
            "\t</Style>\n" +

            "\t<Folder>\n")

        for tower in towers:
            kml_file.write(
                "\t\t\t<Placemark>\n" +
                "\t\t\t\t<name>" + tower.name + "</name>\n" +
                "\t\t\t\t<visibility>1</visibility>\n" +
                "\t\t\t\t<styleUrl>#tower</styleUrl>\n" +
                "\t\t\t\t<Point>\n" +
                "\t\t\t\t\t<coordinates>" + str(tower.longitude) +","+
                str(tower.latitude) +","+ str(tower.altitude) +
                "</coordinates>\n" +
                "\t\t\t\t</Point>\n" +
                "\t\t\t</Placemark>\n")

        kml_file.write(
            "\t\t</Folder>\n" +
            "\t</Document>\n" +
            "</kml>\n")

        kml_file.close()
        return filename
