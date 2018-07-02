from osgeo import ogr
import fiona
from shapely.geometry import mapping
from pywps import Process, ComplexInput, LiteralOutput, Format


class TotalLength(Process):
    """Process calculating area of given polygon
    """
    def __init__(self):
        inputs = [ComplexInput('layer', 'Layer',
                               [Format('application/gml+xml')])]
        outputs = [LiteralOutput('total', 'Total', data_type='string')]

        super(TotalLength, self).__init__(
            self.gml_handler,
            identifier='total_length',
            title='Process Total Length',
            abstract="""Process returns the total length of all
                lines in a submitted GML file""",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def gml_handler(self, request, response):
        """GML version of the handler

        Calculate total length of the input lines
        """

        input_gml = request.inputs['layer'][0].file
        driver = ogr.GetDriverByName("GML")

        dataSource = driver.Open(input_gml, 0)
        layer = dataSource.GetLayer()
        total = 0
        for feature in layer:
            total = total + feature.length
        response.outputs['total'].data = str(total)
        return response

    def fiona_handler(self, request, response):
        """Shapely version of the handler

        Calculate total length of the input lines
        """

        with fiona.open(request.inputs['layer'][0].file) as data_file:

            length = 0
            for feature in data_file:
                geom = mapping(feature["geometry"])
                length += geom.length

            response.outputs['total'].data = str(length)
            return response
