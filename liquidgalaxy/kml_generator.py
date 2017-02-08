import os
import zipfile
from idivt.models import Tower


def create_line_kml2(line, towers):
    filename = "static/kml/" + line.name + ".kml"
    image1 = "http://maps.google.com/mapfiles/kml/shapes/star.png"
    if os.path.exists(filename):
            os.system("rm " + filename)
    os.system("touch " + filename)
    with open(filename, "w") as kml_file:
        kml_file.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\" ?>\n" +
            "<kml xmlns=\"http://www.opengis.net/kml/2.2\" xmlns:gx=\"http://www.google.com/kml/ext/2.2\">\n" +
            "\t<Folder>\n")

        for tower in towers:
            kml_file.write(

                "\t\t<Placemark>\n"+
                "\t\t\t\t<name>" + tower.name + "</name>\n" +
                "\t\t\t<Style id=\""+str(tower.pk)+"\" />\n" +
                "\t\t\t<Model>\n" +
                "\t\t\t\t<altitudeMode>relativeToGround</altitudeMode>\n" +
                "\t\t\t\t<Location>\n" +
                "\t\t\t\t\t<latitude>"+str(tower.latitude)+"</latitude>\n" +
                "\t\t\t\t\t<longitude>"+str(tower.longitude)+"</longitude>\n" +
                "\t\t\t\t\t<altitude>"+str(tower.altitude)+"</altitude>\n" +
                "\t\t\t\t</Location>\n" +
                "\t\t\t\t<Orientation>\n" +
                "\t\t\t\t\t<heading>358.4156652213</heading>\n" +
                "\t\t\t\t\t<tilt>0</tilt>\n" +
                "\t\t\t\t\t<roll>0</roll>\n" +
                "\t\t\t\t</Orientation>\n" +
                "\t\t\t\t<Scale><x>1</x><y>1</y><z>1</z></Scale>\n" +
                "\t\t\t\t<Link><href>models/untitled.dae</href></Link>\n" +
                "\t\t\t</Model>\n" +
                "\t\t</Placemark>\n")

            kml_file.write(
                "\t\t\t<Placemark>\n" +
                "\t\t\t\t<name>" + tower.name + "</name>\n" +
                "\t\t\t\t<visibility>1</visibility>\n" +
                "\t\t\t\t<Point>\n" +
                "\t\t\t\t\t<coordinates>" + str(tower.longitude) +","+
                str(tower.latitude) +","+ str(tower.altitude) +
                "</coordinates>\n" +
                "\t\t\t\t</Point>\n" +
                "\t\t\t</Placemark>\n")

        kml_file.write("\t</Folder>\n" + "</kml>\n")

        kml_file.close()
        return filename


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
            "\t\t\t\t<href>models/untitled.dae</href>\n" +
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

def create_line_kmz(line, folderKML, folderImg, sufix):
    os.system('rm '+folderKML+line.name+'*.kmz')
    zf = zipfile.ZipFile(folderKML+line.name+str(sufix)+'.kmz', mode='w')
    try:
        zf.write(folderKML+line.name+'.kml', line.name+'.kml', zipfile.ZIP_DEFLATED)
        zf.write(folderImg+'models/untitled.dae', 'models//untitled.dae', zipfile.ZIP_DEFLATED)
        zf.write(folderImg+'models/untitled/texture.png', 'models//untitled//texture.png', zipfile.ZIP_DEFLATED)
        zf.write(folderImg+'models/untitled/texture_0.png', 'models//untitled//texture_0.png', zipfile.ZIP_DEFLATED)
        zf.write(folderImg+'models/untitled/texture_1.png', 'models//untitled//texture_1.png', zipfile.ZIP_DEFLATED)
    finally:
        zf.close()

def create_rotation_kml(line):
    positions = Tower.objects.all().filter(line=line)
    middlePosition = positions[len(positions)/2]

    return create_rotation_kml_aux(middlePosition)


def create_rotation_kml_aux(middlePosition):

    filename = "static/kml/rotation.kml"

    os.system("touch %s" % (filename))

    with open(filename, "w") as kml_file:
        kml_file.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
            "<kml xmlns=\"http://www.opengis.net/kml/2.2\" xmlns:gx=\"http://www.google.com/kml/ext/2.2\">\n" +
            "\t<gx:Tour>\n" +
            "\t\t<name>line</name>\n" +
            "\t\t<gx:Playlist>\n")
        for grades in range(0,360,11):
            kml_file.write(
                "\t\t<gx:FlyTo>\n" +
                "\t\t\t<gx:duration>5.0</gx:duration>\n" +
                "\t\t\t<gx:flyToMode>smooth</gx:flyToMode>\n" +
                            "\t\t\t\t<LookAt>\n" +
                            "\t\t\t\t\t<longitude>"+ str(middlePosition.longitude) +"</longitude>\n" +
                            "\t\t\t\t\t<latitude>"+ str(middlePosition.latitude) +"</latitude>\n" +
                            "\t\t\t\t\t<altitude>0</altitude>\n" +
                            "\t\t\t\t\t<heading>"+str(grades)+"</heading>\n" +
                            "\t\t\t\t\t<range>6000</range>\n" +
                            "\t\t\t\t\t<tilt>80</tilt>\n" +
                            "\t\t\t\t\t<altitudeMode>relativeToGround</altitudeMode>\n" +
                            "\t\t\t\t</LookAt>\n" +
                            "\t\t</gx:FlyTo>\n"
                            )
        kml_file.write(
            "\t\t</gx:Playlist>\n" +
            "\t</gx:Tour>\n" +
            "</kml>\n"
        )
        kml_file.close()
        return filename
